
(cl:in-package :asdf)

(defsystem "DriveMotors-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "Rfid" :depends-on ("_package_Rfid"))
    (:file "_package_Rfid" :depends-on ("_package"))
  ))