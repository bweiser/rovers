FILE(REMOVE_RECURSE
  "src/DirectionButtons/msg"
  "src/DirectionButtons/srv"
  "msg_gen"
  "srv_gen"
  "msg_gen"
  "srv_gen"
  "CMakeFiles/ROSBUILD_gensrv_lisp"
  "srv_gen/lisp/Lamp.lisp"
  "srv_gen/lisp/_package.lisp"
  "srv_gen/lisp/_package_Lamp.lisp"
)

# Per-language clean rules from dependency scanning.
FOREACH(lang)
  INCLUDE(CMakeFiles/ROSBUILD_gensrv_lisp.dir/cmake_clean_${lang}.cmake OPTIONAL)
ENDFOREACH(lang)
