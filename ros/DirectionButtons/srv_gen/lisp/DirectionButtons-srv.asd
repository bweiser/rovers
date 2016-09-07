
(cl:in-package :asdf)

(defsystem "DirectionButtons-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Lamp" :depends-on ("_package_Lamp"))
    (:file "_package_Lamp" :depends-on ("_package"))
  ))