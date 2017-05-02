[1mdiff --git a/.idea/SP_Wait.sql b/.idea/SP_Wait.sql[m
[1mindex e69de29..26a43b5 100644[m
[1m--- a/.idea/SP_Wait.sql[m
[1m+++ b/.idea/SP_Wait.sql[m
[36m@@ -0,0 +1,94 @@[m
[32m+[m[32mUSE [msdb][m
[32m+[m[32mGO[m
[32m+[m[32mSET ANSI_NULLS ON[m
[32m+[m[32mGO[m
[32m+[m[32mSET QUOTED_IDENTIFIER OFF[m
[32m+[m[32mIf Exists (select * from sysobjects where type='p'and name= 'SP_wait')[m
[32m+[m[32mBegin[m
[32m+[m	[32mDrop procedure [dbo].[SP_wait][m
[32m+[m[32mEnd[m
[32m+[m[32mGO[m
[32m+[m[32mCreate PROCEDURE [dbo].[SP_wait][m
[32m+[m[32m([m
[32m+[m[32m@job_name SYSNAME,[m
[32m+[m[32m@WaitTime DATETIME = '00:10:00',[m
[32m+[m[32m@JobCompletionStatus INT = null OUTPUT[m
[32m+[m[32m)[m
[32m+[m[32mAS[m
[32m+[m
[32m+[m[32mSET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED[m
[32m+[m[32mSET NOCOUNT ON[m
[32m+[m
[32m+[m[32mDECLARE @job_id            UNIQUEIDENTIFIER[m
[32m+[m[32mDECLARE @job_owner   sysname[m
[32m+[m
[32m+[m[32mCREATE TABLE #KAP (job_id             UNIQUEIDENTIFIER NOT NULL,[m
[32m+[m[32m                        last_run_date         INT              NOT NULL,[m
[32m+[m[32m                        last_run_time         INT              NOT NULL,[m
[32m+[m[32m                        next_run_date         INT              NOT NULL,[m
[32m+[m[32m                        next_run_time         INT              NOT NULL,[m
[32m+[m[32m                        next_run_schedule_id  INT              NOT NULL,[m
[32m+[m[32m                        requested_to_run      INT              NOT NULL, -- BOOL[m
[32m+[m[32m                        request_source        INT              NOT NULL,[m
[32m+[m[32m                        request_source_id     sysname          COLLATE database_default NULL,[m
[32m+[m[32m                        running               INT              NOT NULL, -- BOOL[m
[32m+[m[32m                        current_step          INT              NOT NULL,[m
[32m+[m[32m                        current_retry_attempt INT              NOT NULL,[m
[32m+[m[32m                        job_state             INT              NOT NULL)[m
[32m+[m
[32m+[m[32mSELECT @job_id = job_id FROM msdb.dbo.sysjobs[m
[32m+[m[32mWHERE name = @job_name[m
[32m+[m
[32m+[m[32mSELECT @job_owner = SUSER_SNAME()[m
[32m+[m
[32m+[m[32mINSERT INTO #KAP[m
[32m+[m[32mEXECUTE master.dbo.xp_sqlagent_enum_jobs  1, @job_owner, @job_id[m
[32m+[m
[32m+[m[32m-- Start the job if the job is not running[m
[32m+[m[32mIF NOT EXISTS(SELECT TOP 1 * FROM #KAP WHERE running = 1)[m
[32m+[m[32m       EXEC msdb.dbo.sp_start_job @job_name = @job_name[m
[32m+[m
[32m+[m[32m-- Give 2 sec for think time.[m
[32m+[m[32mWAITFOR DELAY '00:00:02'[m
[32m+[m
[32m+[m[32mDELETE FROM #KAP[m
[32m+[m[32mINSERT INTO #KAP[m
[32m+[m[32mEXECUTE master.dbo.xp_sqlagent_enum_jobs  1, @job_owner, @job_id[m
[32m+[m
[32m+[m[32mWHILE EXISTS(SELECT TOP 1 * FROM #KAP WHERE running = 1)[m
[32m+[m[32mBEGIN[m
[32m+[m
[32m+[m[32m       WAITFOR DELAY @WaitTime[m
[32m+[m
[32m+[m[32m       -- Information[m
[32m+[m[32m       raiserror('JOB IS RUNNING', 0, 1 ) WITH NOWAIT[m
[32m+[m
[32m+[m[32m       DELETE FROM #KAP[m
[32m+[m
[32m+[m[32m       INSERT INTO #KAP[m
[32m+[m[32m       EXECUTE master.dbo.xp_sqlagent_enum_jobs  1, @job_owner, @job_id[m
[32m+[m
[32m+[m[32mEND[m
[32m+[m
[32m+[m[32mSELECT @JobCompletionStatus = run_status[m
[32m+[m[32mFROM msdb.dbo.sysjobhistory[m
[32m+[m[32mWHERE job_id = @job_id[m
[32m+[m
[32m+[m[32mIF @JobCompletionStatus = 1[m
[32m+[m[32mbegin[m
[32m+[m[32m       PRINT 'The job ran Successful'[m
[32m+[m	[32m   EXEC dbo.sp_update_job[m
[32m+[m[32m       @job_name = @JOB_NAME,@enabled = 0[m
[32m+[m	[32m   PRINT 'The job'+@JOB_NAME+ 'Disabled Successfully'[m
[32m+[m	[32m   END[m
[32m+[m
[32m+[m
[32m+[m[32mELSE IF @JobCompletionStatus = 3[m
[32m+[m[32m       PRINT 'The job'+@JOB_NAME+' is Cancelled'[m
[32m+[m[32mELSE[m
[32m+[m[32mBEGIN[m
[32m+[m[32m       RAISERROR ('[ERROR]:%s job is either failed or not in good state. Please check',16, 1, @job_name) WITH LOG[m
[32m+[m[32mEND[m
[32m+[m
[32m+[m[32mRETURN @JobCompletionStatus[m
[32m+[m
[1mdiff --git a/.idea/workspace.xml b/.idea/workspace.xml[m
[1mindex af90496..e46fab8 100644[m
[1m--- a/.idea/workspace.xml[m
[1m+++ b/.idea/workspace.xml[m
[36m@@ -2,8 +2,10 @@[m
 <project version="4">[m
   <component name="ChangeListManager">[m
     <list default="true" id="61b103d9-ab08-46cf-91a9-3dc2671c5e36" name="Default" comment="">[m
[32m+[m[32m      <change type="NEW" beforePath="" afterPath="$PROJECT_DIR$/.idea/SP_Wait.sql" />[m
[32m+[m[32m      <change type="NEW" beforePath="" afterPath="$PROJECT_DIR$/.idea/dbnavigator.xml" />[m
[32m+[m[32m      <change type="NEW" beforePath="" afterPath="$PROJECT_DIR$/SP_Wait.py" />[m
       <change type="MODIFICATION" beforePath="$PROJECT_DIR$/.idea/workspace.xml" afterPath="$PROJECT_DIR$/.idea/workspace.xml" />[m
[31m-      <change type="MODIFICATION" beforePath="$PROJECT_DIR$/DashBoad_Create.py" afterPath="$PROJECT_DIR$/DashBoad_Create.py" />[m
     </list>[m
     <option name="EXCLUDED_CONVERTED_TO_IGNORED" value="true" />[m
     <option name="TRACKING_ENABLED" value="true" />[m
[36m@@ -18,21 +20,41 @@[m
   <component name="ExecutionTargetManager" SELECTED_TARGET="default_target" />[m
   <component name="FileEditorManager">[m
     <leaf SIDE_TABS_SIZE_LIMIT_KEY="375">[m
[32m+[m[32m      <file leaf-file-name="baseFile.py" pinned="false" current-in-tab="false">[m
[32m+[m[32m        <entry file="file://$PROJECT_DIR$/../Github_Network-Scripting/Project_OSPF/baseFile.py">[m
[32m+[m[32m          <provider selected="true" editor-type-id="text-editor">[m
[32m+[m[32m            <state relative-caret-position="544">[m
[32m+[m[32m              <caret line="34" column="0" lean-forward="false" selection-start-line="34" selection-start-column="0" selection-end-line="34" selection-end-column="0" />[m
[32m+[m[32m              <folding />[m
[32m+[m[32m            </state>[m
[32m+[m[32m          </provider>[m
[32m+[m[32m        </entry>[m
[32m+[m[32m      </file>[m
       <file leaf-file-name="OOP1.py" pinned="false" current-in-tab="false">[m
         <entry file="file://$PROJECT_DIR$/OOP1.py">[m
           <provider selected="true" editor-type-id="text-editor">[m
[31m-            <state relative-caret-position="116">[m
[32m+[m[32m            <state relative-caret-position="153">[m
               <caret line="9" column="42" lean-forward="false" selection-start-line="9" selection-start-column="42" selection-end-line="10" selection-end-column="41" />[m
               <folding />[m
             </state>[m
           </provider>[m
         </entry>[m
       </file>[m
[31m-      <file leaf-file-name="DashBoad_Create.py" pinned="false" current-in-tab="true">[m
[32m+[m[32m      <file leaf-file-name="DashBoad_Create.py" pinned="false" current-in-tab="false">[m
         <entry file="file://$PROJECT_DIR$/DashBoad_Create.py">[m
           <provider selected="true" editor-type-id="text-editor">[m
[31m-            <state relative-caret-position="186">[m
[31m-              <caret line="6" column="19" lean-forward="true" selection-start-line="6" selection-start-column="19" selection-end-line="6" selection-end-column="19" />[m
[32m+[m[32m            <state relative-caret-position="102">[m
[32m+[m[32m              <caret line="6" column="19" lean-forward="false" selection-start-line="6" selection-start-column="19" selection-end-line="6" selection-end-column="19" />[m
[32m+[m[32m              <folding />[m
[32m+[m[32m            </state>[m
[32m+[m[32m          </provider>[m
[32m+[m[32m        </entry>[m
[32m+[m[32m      </file>[m
[32m+[m[32m      <file leaf-file-name="SP_Wait.sql" pinned="false" current-in-tab="true">[m
[32m+[m[32m        <entry file="file://$PROJECT_DIR$/.idea/SP_Wait.sql">[m
[32m+[m[32m          <provider selected="true" editor-type-id="text-editor">[m
[32m+[m[32m            <state relative-caret-position="540">[m
[32m+[m[32m              <caret line="66" column="0" lean-forward="true" selection-start-line="66" selection-start-column="0" selection-end-line="66" selection-end-column="0" />[m
               <folding />[m
             </state>[m
           </provider>[m
[36m@@ -74,20 +96,23 @@[m
         <option value="$PROJECT_DIR$/TestCase-1" />[m
         <option value="$PROJECT_DIR$/.idea/OOP.py" />[m
         <option value="$PROJECT_DIR$/DashBoad_Create.py" />[m
[32m+[m[32m        <option value="$PROJECT_DIR$/../Github_Network-Scripting/Project_OSPF/baseFile.py" />[m
[32m+[m[32m        <option value="$PROJECT_DIR$/SP_Wait.py" />[m
[32m+[m[32m        <option value="$PROJECT_DIR$/.idea/SP_Wait.sql" />[m
       </list>[m
     </option>[m
   </component>[m
   <component name="ProjectFrameBounds">[m
[31m-    <option name="x" value="-8" />[m
[32m+[m[32m    <option name="x" value="1592" />[m
     <option name="y" value="-8" />[m
[31m-    <option name="width" value="1616" />[m
[31m-    <option name="height" value="876" />[m
[32m+[m[32m    <option name="width" value="1936" />[m
[32m+[m[32m    <option name="height" value="1056" />[m
   </component>[m
   <component name="ProjectLevelVcsManager">[m
     <ConfirmationsSetting value="2" id="Add" />[m
   </component>[m
   <component name="ProjectView">[m
[31m-    <navigator currentView="ProjectPane" proportions="" version="1">[m
[32m+[m[32m    <navigator proportions="" version="1">[m
       <flattenPackages />[m
       <showMembers />[m
       <showModules />[m
[36m@@ -100,28 +125,11 @@[m
       <manualOrder />[m
       <foldersAlwaysOnTop value="true" />[m
     </navigator>[m
[31m-    <panes>[m
[31m-      <pane id="Scratches" />[m
[31m-      <pane id="Scope" />[m
[31m-      <pane id="ProjectPane">[m
[31m-        <subPane>[m
[31m-          <PATH>[m
[31m-            <PATH_ELEMENT>[m
[31m-              <option name="myItemId" value="PythonLearningProg" />[m
[31m-              <option name="myItemType" value="com.intellij.ide.projectView.impl.nodes.ProjectViewProjectNode" />[m
[31m-            </PATH_ELEMENT>[m
[31m-            <PATH_ELEMENT>[m
[31m-              <option name="myItemId" value="PythonLearningProg" />[m
[31m-              <option name="myItemType" value="com.intellij.ide.projectView.impl.nodes.PsiDirectoryNode" />[m
[31m-            </PATH_ELEMENT>[m
[31m-          </PATH>[m
[31m-        </subPane>[m
[31m-      </pane>[m
[31m-    </panes>[m
[32m+[m[32m    <panes />[m
   </component>[m
   <component name="PropertiesComponent">[m
[31m-    <property name="settings.editor.selected.configurable" value="preferences.general" />[m
[31m-    <property name="last_opened_file_path" value="$PROJECT_DIR$" />[m
[32m+[m[32m    <property name="settings.editor.selected.configurable" value="configurable.group.tools" />[m
[32m+[m[32m    <property name="last_opened_file_path" value="$PROJECT_DIR$/../Github_Network-Scripting/Project_OSPF/baseFile.py" />[m
   </component>[m
   <component name="PyConsoleOptionsProvider">[m
     <option name="myShowDebugConsoleByDefault" value="true" />[m
[36m@@ -394,19 +402,26 @@[m
     <servers />[m
   </component>[m
   <component name="ToolWindowManager">[m
[31m-    <frame x="-8" y="-8" width="1616" height="876" extended-state="6" />[m
[32m+[m[32m    <frame x="1592" y="-8" width="1936" height="1056" extended-state="7" />[m
     <editor active="true" />[m
     <layout>[m
[31m-      <window_info id="Project" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.12125" sideWeight="0.5" order="1" side_tool="false" content_ui="combo" />[m
       <window_info id="TODO" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="9" side_tool="false" content_ui="tabs" />[m
[31m-      <window_info id="Event Log" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="0" side_tool="true" content_ui="tabs" />[m
[31m-      <window_info id="Run" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="true" show_stripe_button="true" weight="0.336875" sideWeight="0.5" order="4" side_tool="false" content_ui="tabs" />[m
[32m+[m[32m      <window_info id="DB Browser" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="-1" side_tool="false" content_ui="tabs" />[m
[32m+[m[32m      <window_info id="DB Execution Console" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="-1" side_tool="false" content_ui="tabs" />[m
[32m+[m[32m      <window_info id="Event Log" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.32885906" sideWeight="0.5" order="0" side_tool="true" content_ui="tabs" />[m
       <window_info id="Version Control" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="1" side_tool="false" content_ui="tabs" />[m
       <window_info id="Python Console" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />[m
[31m-      <window_info id="Structure" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />[m
[32m+[m[32m      <window_info id="Run" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.336875" sideWeight="0.5" order="4" side_tool="false" content_ui="tabs" />[m
       <window_info id="Terminal" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.32885906" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />[m
[31m-      <window_info id="Debug" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="6" side_tool="false" content_ui="tabs" />[m
[32m+[m[32m      <window_info id="Project" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.12125" sideWeight="0.5" order="1" side_tool="false" content_ui="combo" />[m
[32m+[m[32m      <window_info id="MaxCompute Console" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="-1" side_tool="false" content_ui="tabs" />[m
[32m+[m[32m      <window_info id="MaxCompute Job Explorer" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="-1" side_tool="false" content_ui="tabs" />[m
[32m+[m[32m      <window_info id="Running Info" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="-1" side_tool="false" content_ui="tabs" />[m
[32m+[m[32m      <window_info id="Structure" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="2" side_tool="false" content_ui="tabs" />[m
[32m+[m[32m      <window_info id="Running Result" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="-1" side_tool="true" content_ui="tabs" />[m
       <window_info id="Favorites" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="0" side_tool="true" content_ui="tabs" />[m
[32m+[m[32m      <window_info id="MaxCompute Project Explorer" active="false" anchor="left" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="-1" side_tool="false" content_ui="tabs" />[m
[32m+[m[32m      <window_info id="Debug" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.4" sideWeight="0.5" order="6" side_tool="false" content_ui="tabs" />[m
       <window_info id="Data View" active="false" anchor="right" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="3" side_tool="false" content_ui="tabs" />[m
       <window_info id="Cvs" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.25" sideWeight="0.5" order="7" side_tool="false" content_ui="tabs" />[m
       <window_info id="Message" active="false" anchor="bottom" auto_hide="false" internal_type="DOCKED" type="DOCKED" visible="false" show_stripe_button="true" weight="0.33" sideWeight="0.5" order="4" side_tool="false" content_ui="tabs" />[m
[36m@@ -425,35 +440,6 @@[m
     <watches-manager />[m
   </component>[m
   <component name="editorHistoryManager">[m
[31m-    <entry file="file://$PROJECT_DIR$/../Github_Network-Scripting/IpRegEx_3.py">[m
[31m-      <provider selected="true" editor-type-id="text-editor">[m
[31m-        <state relative-caret-position="136">[m
[31m-          <caret line="8" column="21" lean-forward="false" selection-start-line="8" selection-start-column="21" selection-end-line="8" selection-end-column="21" />[m
[31m-        </state>[m
[31m-      </provider>[m
[31m-    </entry>[m
[31m-    <entry file="file://$PROJECT_DIR$/Reg_Prac.py">[m
[31m-      <provider selected="true" editor-type-id="text-editor">[m
[31m-        <state relative-caret-position="170">[m
[31m-          <caret line="10" column="0" lean-forward="false" selection-start-line="10" selection-start-column="0" selection-end-line="10" selection-end-column="0" />[m
[31m-        </state>[m
[31m-      </provider>[m
[31m-    </entry>[m
[31m-    <entry file="file://$PROJECT_DIR$/RobotEX-1">[m
[31m-      <provider selected="true" editor-type-id="text-editor">[m
[31m-        <state relative-caret-position="221">[m
[31m-          <caret line="13" column="27" lean-forward="true" selection-start-line="13" selection-start-column="27" selection-end-line="13" selection-end-column="27" />[m
[31m-          <folding />[m
[31m-        </state>[m
[31m-      </provider>[m
[31m-    </entry>[m
[31m-    <entry file="file://$PROJECT_DIR$/../Github_Network-Scripting/RX_Script.py">[m
[31m-      <provider selected="true" editor-type-id="text-editor">[m
[31m-        <state relative-caret-position="0">[m
[31m-          <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />[m
[31m-        </state>[m
[31m-      </provider>[m
[31m-    </entry>[m
     <entry file="file://$PROJECT_DIR$/RegEx.py">[m
       <provider selected="true" editor-type-id="text-editor">[m
         <state relative-caret-position="11203">[m
[36m@@ -720,7 +706,6 @@[m
       <provider selected="true" editor-type-id="text-editor">[m
         <state relative-caret-position="0">[m
           <caret line="0" column="0" lean-forward="false" selection-start-line="0" selection-start-column="0" selection-end-line="0" selection-end-column="0" />[m
[31m-          <folding />[m
         </state>[m
       </provider>[m
     </entry>[m
[36m@@ -728,7 +713,6 @@[m
       <provider selected="true" editor-type-id="text-editor">[m
         <state relative-caret-position="162">[m
           <caret line="6" column="18" lean-forward="true" selection-start-line="6" selection-start-column="18" selection-end-line="6" selection-end-column="18" />[m
[31m-          <folding />[m
         </state>[m
       </provider>[m
     </entry>[m
[36m@@ -736,7 +720,6 @@[m
       <provider selected="true" editor-type-id="text-editor">[m
         <state relative-caret-position="158">[m
           <caret line="12" column="32" lean-forward="false" selection-start-line="12" selection-start-column="32" selection-end-line="12" selection-end-column="32" />[m
[31m-          <folding />[m
         </state>[m
       </provider>[m
     </entry>[m
[36m@@ -744,30 +727,52 @@[m
       <provider selected="true" editor-type-id="text-editor">[m
         <state relative-caret-position="162">[m
           <caret line="6" column="0" lean-forward="false" selection-start-line="6" selection-start-column="0" selection-end-line="6" selection-end-column="0" />[m
[31m-          <folding />[m
         </state>[m
       </provider>[m
     </entry>[m
[31m-    <entry file="file://$PROJECT_DIR$/.idea/OOP.py">[m
[32m+[m[32m    <entry file="file://$PROJECT_DIR$/.idea/OOP.py" />[m
[32m+[m[32m    <entry file="file://$PROJECT_DIR$/../OSPF_Automation/OSPF_Automation.gns3">[m
[32m+[m[32m      <provider selected="true" editor-type-id="text-editor">[m
[32m+[m[32m        <state relative-caret-position="-3744">[m
[32m+[m[32m          <caret line="18" column="35" lean-forward="false" selection-start-line="18" selection-start-column="35" selection-end-line="18" selection-end-column="35" />[m
[32m+[m[32m        </state>[m
[32m+[m[32m      </provider>[m
[32m+[m[32m    </entry>[m
[32m+[m[32m    <entry file="file://$PROJECT_DIR$/../Github_Network-Scripting/Project_OSPF/baseFile.py">[m
       <provider selected="true" editor-type-id="text-editor">[m
[31m-        <state relative-caret-position="666">[m
[31m-          <caret line="18" column="13" lean-forward="true" selection-start-line="18" selection-start-column="13" selection-end-line="18" selection-end-column="13" />[m
[32m+[m[32m        <state relative-caret-position="544">[m
[32m+[m[32m          <caret line="34" column="0" lean-forward="false" selection-start-line="34" selection-start-column="0" selection-end-line="34" selection-end-column="0" />[m
           <folding />[m
         </state>[m
       </provider>[m
     </entry>[m
     <entry file="file://$PROJECT_DIR$/OOP1.py">[m
       <provider selected="true" editor-type-id="text-editor">[m
[31m-        <state relative-caret-position="116">[m
[32m+[m[32m        <state relative-caret-position="153">[m
           <caret line="9" column="42" lean-forward="false" selection-start-line="9" selection-start-column="42" selection-end-line="10" selection-end-column="41" />[m
           <folding />[m
         </state>[m
       </provider>[m
     </entry>[m
[32m+[m[32m    <entry file="file://$PROJECT_DIR$/SP_Wait.py">[m
[32m+[m[32m      <provider selected="true" editor-type-id="text-editor">[m
[32m+[m[32m        <state relative-caret-position="162">[m
[32m+[m[32m          <caret line="6" column="3" lean-forward="true" selection-start-line="6" selection-start-column="3" selection-end-line="6" selection-end-column="3" />[m
[32m+[m[32m        </state>[m
[32m+[m[32m      </provider>[m
[32m+[m[32m    </entry>[m
     <entry file="file://$PROJECT_DIR$/DashBoad_Create.py">[m
       <provider selected="true" editor-type-id="text-editor">[m
[31m-        <state relative-caret-position="186">[m
[31m-          <caret line="6" column="19" lean-forward="true" selection-start-line="6" selection-start-column="19" selection-end-line="6" selection-end-column="19" />[m
[32m+[m[32m        <state relative-caret-position="102">[m
[32m+[m[32m          <caret line="6" column="19" lean-forward="false" selection-start-line="6" selection-start-column="19" selection-end-line="6" selection-end-column="19" />[m
[32m+[m[32m          <folding />[m
[32m+[m[32m        </state>[m
[32m+[m[32m      </provider>[m
[32m+[m[32m    </entry>[m
[32m+[m[32m    <entry file="file://$PROJECT_DIR$/.idea/SP_Wait.sql">[m
[32m+[m[32m      <provider selected="true" editor-type-id="text-editor">[m
[32m+[m[32m        <state relative-caret-position="540">[m
[32m+[m[32m          <caret line="66" column="0" lean-forward="true" selection-start-line="66" selection-start-column="0" selection-end-line="66" selection-end-column="0" />[m
           <folding />[m
         </state>[m
       </provider>[m
[1mdiff --git a/SP_Wait.py b/SP_Wait.py[m
[1mindex e69de29..3d36cac 100644[m
[1m--- a/SP_Wait.py[m
[1m+++ b/SP_Wait.py[m
[36m@@ -0,0 +1,252 @@[m
[32m+[m[32mUSE[msdb][m
[32m+[m[32mGO[m
[32m+[m[32mSET[m
[32m+[m[32mANSI_NULLS[m
[32m+[m[32mON[m
[32m+[m[32mGO[m
[32m+[m[32mSET[m
[32m+[m[32mQUOTED_IDENTIFIER[m
[32m+[m[32mOFF[m
[32m+[m[32mIf[m
[32m+[m[32mExists(select *[m
[32m+[m[32mfrom sysobjects where[m
[32m+[m
[32m+[m[32mtype = 'p' and name = 'SP_wait')[m
[32m+[m[32mBegin[m
[32m+[m[32mDrop[m
[32m+[m[32mprocedure[dbo].[SP_wait][m
[32m+[m[32mEnd[m
[32m+[m[32mGO[m
[32m+[m[32mCreate[m
[32m+[m[32mPROCEDURE[dbo].[SP_wait][m
[32m+[m[32m([m
[32m+[m[32m@ job_name[m
[32m+[m[32mSYSNAME,[m
[32m+[m
[32m+[m
[32m+[m[32m@WaitTime[m
[32m+[m
[32m+[m
[32m+[m[32mDATETIME = '00:10:00',[m
[32m+[m
[32m+[m
[32m+[m[32m@JobCompletionStatus[m
[32m+[m
[32m+[m
[32m+[m[32mINT = null[m
[32m+[m[32mOUTPUT[m
[32m+[m[32m)[m
[32m+[m[32mAS[m
[32m+[m
[32m+[m[32mSET[m
[32m+[m[32mTRANSACTION[m
[32m+[m[32mISOLATION[m
[32m+[m[32mLEVEL[m
[32m+[m[32mREAD[m
[32m+[m[32mUNCOMMITTED[m
[32m+[m[32mSET[m
[32m+[m[32mNOCOUNT[m
[32m+[m[32mON[m
[32m+[m
[32m+[m[32mDECLARE @ job_id[m
[32m+[m[32mUNIQUEIDENTIFIER[m
[32m+[m[32mDECLARE @ job_owner[m
[32m+[m[32msysname[m
[32m+[m
[32m+[m[32mCREATE[m
[32m+[m[32mTABLE  # KAP (job_id             UNIQUEIDENTIFIER NOT NULL,[m
[32m+[m[32mlast_run_date[m
[32m+[m[32mINT[m
[32m+[m[32mNOT[m
[32m+[m[32mNULL,[m
[32m+[m[32mlast_run_time[m
[32m+[m[32mINT[m
[32m+[m[32mNOT[m
[32m+[m[32mNULL,[m
[32m+[m[32mnext_run_date[m
[32m+[m[32mINT[m
[32m+[m[32mNOT[m
[32m+[m[32mNULL,[m
[32m+[m[32mnext_run_time[m
[32m+[m[32mINT[m
[32m+[m[32mNOT[m
[32m+[m[32mNULL,[m
[32m+[m[32mnext_run_schedule_id[m
[32m+[m[32mINT[m
[32m+[m[32mNOT[m
[32m+[m[32mNULL,[m
[32m+[m[32mrequested_to_run[m
[32m+[m[32mINT[m
[32m+[m[32mNOT[m
[32m+[m[32mNULL, -- BOOL[m
[32m+[m[32mrequest_source[m
[32m+[m[32mINT[m
[32m+[m[32mNOT[m
[32m+[m[32mNULL,[m
[32m+[m[32mrequest_source_id[m
[32m+[m[32msysname[m
[32m+[m[32mCOLLATE[m
[32m+[m[32mdatabase_default[m
[32m+[m[32mNULL,[m
[32m+[m[32mrunning[m
[32m+[m[32mINT[m
[32m+[m[32mNOT[m
[32m+[m[32mNULL, -- BOOL[m
[32m+[m[32mcurrent_step[m
[32m+[m[32mINT[m
[32m+[m[32mNOT[m
[32m+[m[32mNULL,[m
[32m+[m[32mcurrent_retry_attempt[m
[32m+[m[32mINT[m
[32m+[m[32mNOT[m
[32m+[m[32mNULL,[m
[32m+[m[32mjob_state[m
[32m+[m[32mINT[m
[32m+[m[32mNOT[m
[32m+[m[32mNULL)[m
[32m+[m
[32m+[m[32mSELECT @ job_id = job_id[m
[32m+[m[32mFROM[m
[32m+[m[32mmsdb.dbo.sysjobs[m
[32m+[m[32mWHERE[m
[32m+[m[32mname =[m
[32m+[m
[32m+[m
[32m+[m[32m@job_name[m
[32m+[m
[32m+[m
[32m+[m[32mSELECT @ job_owner = SUSER_SNAME()[m
[32m+[m
[32m+[m[32mINSERT[m
[32m+[m[32mINTO  # KAP[m
[32m+[m[32mEXECUTE[m
[32m+[m[32mmaster.dbo.xp_sqlagent_enum_jobs[m
[32m+[m[32m1,[m
[32m+[m
[32m+[m
[32m+[m[32m@job_owner[m
[32m+[m
[32m+[m[32m, @job_id[m
[32m+[m
[32m+[m
[32m+[m[32m-- Start[m
[32m+[m[32mthe[m
[32m+[m[32mjob if the[m
[32m+[m[32mjob is not running[m
[32m+[m[32mIF[m
[32m+[m[32mNOT[m
[32m+[m[32mEXISTS(SELECT[m
[32m+[m[32mTOP[m
[32m+[m[32m1 * FROM  # KAP WHERE running = 1)[m
[32m+[m[32mEXEC[m
[32m+[m[32mmsdb.dbo.sp_start_job @ job_name =[m
[32m+[m
[32m+[m
[32m+[m[32m@job_name[m
[32m+[m
[32m+[m
[32m+[m[32m-- Give[m
[32m+[m[32m2[m
[32m+[m[32msec[m
[32m+[m[32mfor think time.[m
[32m+[m[32m    WAITFOR[m
[32m+[m[32m    DELAY[m
[32m+[m[32m    '00:00:02'[m
[32m+[m
[32m+[m[32mDELETE[m
[32m+[m[32mFROM  # KAP[m
[32m+[m[32mINSERT[m
[32m+[m[32mINTO  # KAP[m
[32m+[m[32mEXECUTE[m
[32m+[m[32mmaster.dbo.xp_sqlagent_enum_jobs[m
[32m+[m[32m1,[m
[32m+[m
[32m+[m
[32m+[m[32m@job_owner[m
[32m+[m
[32m+[m[32m, @job_id[m
[32m+[m
[32m+[m
[32m+[m[32mWHILE[m
[32m+[m[32mEXISTS(SELECT[m
[32m+[m[32mTOP[m
[32m+[m[32m1 * FROM  # KAP WHERE running = 1)[m
[32m+[m[32mBEGIN[m
[32m+[m
[32m+[m[32mWAITFOR[m
[32m+[m[32mDELAY @ WaitTime[m
[32m+[m
[32m+[m[32m- - Information[m
[32m+[m[32mraiserror('JOB IS RUNNING', 0, 1)[m
[32m+[m[32mWITH[m
[32m+[m[32mNOWAIT[m
[32m+[m
[32m+[m[32mDELETE[m
[32m+[m[32mFROM  # KAP[m
[32m+[m
[32m+[m[32mINSERT[m
[32m+[m[32mINTO  # KAP[m
[32m+[m[32mEXECUTE[m
[32m+[m[32mmaster.dbo.xp_sqlagent_enum_jobs[m
[32m+[m[32m1,[m
[32m+[m
[32m+[m
[32m+[m[32m@job_owner[m
[32m+[m
[32m+[m[32m, @job_id[m
[32m+[m
[32m+[m
[32m+[m[32mEND[m
[32m+[m
[32m+[m[32mSELECT @ JobCompletionStatus = run_status[m
[32m+[m[32mFROM[m
[32m+[m[32mmsdb.dbo.sysjobhistory[m
[32m+[m[32mWHERE[m
[32m+[m[32mjob_id =[m
[32m+[m
[32m+[m
[32m+[m[32m@job_id[m
[32m+[m
[32m+[m
[32m+[m[32mIF @ JobCompletionStatus = 1[m
[32m+[m[32mbegin[m
[32m+[m[32mPRINT[m
[32m+[m[32m'The job ran Successful'[m
[32m+[m[32mEXEC[m
[32m+[m[32mdbo.sp_update_job[m
[32m+[m[32m@ job_name =[m
[32m+[m
[32m+[m
[32m+[m[32m@JOB_NAME[m
[32m+[m
[32m+[m[32m, @enabled[m
[32m+[m
[32m+[m[32m= 0[m
[32m+[m[32mPRINT[m
[32m+[m[32m'The job' +[m
[32m+[m
[32m+[m
[32m+[m[32m@JOB_NAME[m
[32m+[m
[32m+[m
[32m+[m[32m+ 'Disabled Successfully'[m
[32m+[m[32mEND[m
[32m+[m
[32m+[m[32mELSE[m
[32m+[m[32mIF @ JobCompletionStatus = 3[m
[32m+[m[32mPRINT[m
[32m+[m[32m'The job' +[m
[32m+[m
[32m+[m
[32m+[m[32m@JOB_NAME[m
[32m+[m
[32m+[m
[32m+[m[32m+' is Cancelled'[m
[32m+[m[32mELSE[m
[32m+[m[32mBEGIN[m
[32m+[m[32mRAISERROR('[ERROR]:%s job is either failed or not in good state. Please check', 16, 1, @ job_name) WITH[m
[32m+[m[32mLOG[m
[32m+[m[32mEND[m
[32m+[m
[32m+[m[32mRETURN @ JobCompletionStatus[m
[32m+[m
warning: LF will be replaced by CRLF in .idea/workspace.xml.
The file will have its original line endings in your working directory.
