
(cl:in-package :asdf)

(defsystem "DirectionButtons-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "DirectionButton" :depends-on ("_package_DirectionButton"))
    (:file "_package_DirectionButton" :depends-on ("_package"))
  ))