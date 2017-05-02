USE [msdb]
GO
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER OFF
Create PROCEDURE [dbo].[sp_sp_start_job_wait]

If Exists (select * from sysobjects where type='p'and name= 'SP_wait')
Begin
	Drop procedure [dbo].[SP_wait]
End
GO
Create PROCEDURE [dbo].[SP_wait]
(
@job_name SYSNAME,
@WaitTime DATETIME = '00:10:00',
@JobCompletionStatus INT = null OUTPUT
)
AS

SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED
SET NOCOUNT ON

DECLARE @job_id            UNIQUEIDENTIFIER
DECLARE @job_owner   sysname

CREATE TABLE #KAP (job_id             UNIQUEIDENTIFIER NOT NULL,
                        last_run_date         INT              NOT NULL,
                        last_run_time         INT              NOT NULL,
                        next_run_date         INT              NOT NULL,
                        next_run_time         INT              NOT NULL,
                        next_run_schedule_id  INT              NOT NULL,
                        requested_to_run      INT              NOT NULL, -- BOOL
                        request_source        INT              NOT NULL,
                        request_source_id     sysname          COLLATE database_default NULL,
                        running               INT              NOT NULL, -- BOOL
                        current_step          INT              NOT NULL,
                        current_retry_attempt INT              NOT NULL,
                        job_state             INT              NOT NULL)

SELECT @job_id = job_id FROM msdb.dbo.sysjobs
WHERE name = @job_name

SELECT @job_owner = SUSER_SNAME()

INSERT INTO #KAP
EXECUTE master.dbo.xp_sqlagent_enum_jobs  1, @job_owner, @job_id

-- Start the job if the job is not running
IF NOT EXISTS(SELECT TOP 1 * FROM #KAP WHERE running = 1)
       EXEC msdb.dbo.sp_start_job @job_name = @job_name

-- Give 2 sec for think time.
WAITFOR DELAY '00:00:02'

DELETE FROM #KAP
INSERT INTO #KAP
EXECUTE master.dbo.xp_sqlagent_enum_jobs  1, @job_owner, @job_id

WHILE EXISTS(SELECT TOP 1 * FROM #KAP WHERE running = 1)
BEGIN

       WAITFOR DELAY @WaitTime

       -- Information
       raiserror('JOB IS RUNNING', 0, 1 ) WITH NOWAIT

       DELETE FROM #KAP

       INSERT INTO #KAP
       EXECUTE master.dbo.xp_sqlagent_enum_jobs  1, @job_owner, @job_id

END

SELECT @JobCompletionStatus = run_status
FROM msdb.dbo.sysjobhistory
WHERE job_id = @job_id

IF @JobCompletionStatus = 1
begin
       PRINT 'The job ran Successful'
	   EXEC dbo.sp_update_job
       @job_name = @JOB_NAME,@enabled = 0
	   PRINT 'The job'+@JOB_NAME+ 'Disabled Successfully'
	   END


ELSE IF @JobCompletionStatus = 3
       PRINT 'The job'+@JOB_NAME+' is Cancelled'
ELSE
BEGIN
       RAISERROR ('[ERROR]:%s job is either failed or not in good state. Please check',16, 1, @job_name) WITH LOG
END

RETURN @JobCompletionStatus

