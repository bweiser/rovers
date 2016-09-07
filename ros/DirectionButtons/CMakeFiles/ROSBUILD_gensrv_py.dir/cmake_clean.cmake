FILE(REMOVE_RECURSE
  "src/DirectionButtons/msg"
  "src/DirectionButtons/srv"
  "msg_gen"
  "srv_gen"
  "msg_gen"
  "srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_py"
  "src/DirectionButtons/srv/__init__.py"
  "src/DirectionButtons/srv/_Lamp.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
