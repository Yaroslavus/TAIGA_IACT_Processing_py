import sys
import sy_iact_func as f

f.main_menu()
ans_2 = f.processing_menu()
ans_3 = f.temporary_files_menu()
f.checker (ans_2, ans_3)

try : f.destroy_temporary_files(ans_3)
except: pass

f.start_processing ()
f.destroy_temporary_files(ans_3)
