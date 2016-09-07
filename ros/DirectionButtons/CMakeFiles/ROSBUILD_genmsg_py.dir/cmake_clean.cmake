FILE(REMOVE_RECURSE
  "src/DirectionButtons/msg"
  "src/DirectionButtons/srv"
  "msg_gen"
  "srv_gen"
  "msg_gen"
  "srv_gen"
  "CMakeFiles/ROSBUILD_genmsg_py"
  "src/DirectionButtons/msg/__init__.py"
  "src/DirectionButtons/msg/_DirectionButton.py"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_genmsg_py.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
