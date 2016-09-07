; Auto-generated. Do not edit!


(cl:in-package DirectionButtons-msg)


;//! \htmlinclude DirectionButton.msg.html

(cl:defclass <DirectionButton> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (buttonEvent
    :reader buttonEvent
    :initarg :buttonEvent
    :type cl:string
    :initform ""))
)

(cl:defclass DirectionButton (<DirectionButton>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <DirectionButton>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'DirectionButton)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name DirectionButtons-msg:<DirectionButton> is deprecated: use DirectionButtons-msg:DirectionButton instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <DirectionButton>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader DirectionButtons-msg:header-val is deprecated.  Use DirectionButtons-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'buttonEvent-val :lambda-list '(m))
(cl:defmethod buttonEvent-val ((m <DirectionButton>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader DirectionButtons-msg:buttonEvent-val is deprecated.  Use DirectionButtons-msg:buttonEvent instead.")
  (buttonEvent m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <DirectionButton>) ostream)
  "Serializes a message object of type '<DirectionButton>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'buttonEvent))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'buttonEvent))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <DirectionButton>) istream)
  "Deserializes a message object of type '<DirectionButton>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'buttonEvent) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'buttonEvent) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<DirectionButton>)))
  "Returns string type for a message object of type '<DirectionButton>"
  "DirectionButtons/DirectionButton")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'DirectionButton)))
  "Returns string type for a message object of type 'DirectionButton"
  "DirectionButtons/DirectionButton")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<DirectionButton>)))
  "Returns md5sum for a message object of type '<DirectionButton>"
  "9df72beb13d34aac7e6eea37f77e9299")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'DirectionButton)))
  "Returns md5sum for a message object of type 'DirectionButton"
  "9df72beb13d34aac7e6eea37f77e9299")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<DirectionButton>)))
  "Returns full string definition for message of type '<DirectionButton>"
  (cl:format cl:nil "#~%# the direction (joystick) or button event~%#~%Header header~%string buttonEvent~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'DirectionButton)))
  "Returns full string definition for message of type 'DirectionButton"
  (cl:format cl:nil "#~%# the direction (joystick) or button event~%#~%Header header~%string buttonEvent~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <DirectionButton>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:length (cl:slot-value msg 'buttonEvent))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <DirectionButton>))
  "Converts a ROS message object to a list"
  (cl:list 'DirectionButton
    (cl:cons ':header (header msg))
    (cl:cons ':buttonEvent (buttonEvent msg))
))
