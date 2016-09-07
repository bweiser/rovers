; Auto-generated. Do not edit!


(cl:in-package DriveMotors-msg)


;//! \htmlinclude Rfid.msg.html

(cl:defclass <Rfid> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (rfidTag
    :reader rfidTag
    :initarg :rfidTag
    :type cl:string
    :initform ""))
)

(cl:defclass Rfid (<Rfid>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Rfid>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Rfid)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name DriveMotors-msg:<Rfid> is deprecated: use DriveMotors-msg:Rfid instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <Rfid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader DriveMotors-msg:header-val is deprecated.  Use DriveMotors-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'rfidTag-val :lambda-list '(m))
(cl:defmethod rfidTag-val ((m <Rfid>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader DriveMotors-msg:rfidTag-val is deprecated.  Use DriveMotors-msg:rfidTag instead.")
  (rfidTag m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Rfid>) ostream)
  "Serializes a message object of type '<Rfid>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'rfidTag))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'rfidTag))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Rfid>) istream)
  "Deserializes a message object of type '<Rfid>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rfidTag) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'rfidTag) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Rfid>)))
  "Returns string type for a message object of type '<Rfid>"
  "DriveMotors/Rfid")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Rfid)))
  "Returns string type for a message object of type 'Rfid"
  "DriveMotors/Rfid")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Rfid>)))
  "Returns md5sum for a message object of type '<Rfid>"
  "e2a6fe4bc703b89049bf2e73727c10e3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Rfid)))
  "Returns md5sum for a message object of type 'Rfid"
  "e2a6fe4bc703b89049bf2e73727c10e3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Rfid>)))
  "Returns full string definition for message of type '<Rfid>"
  (cl:format cl:nil "#~%# the tag ID number for an RFID tag~%#~%Header header~%string rfidTag~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Rfid)))
  "Returns full string definition for message of type 'Rfid"
  (cl:format cl:nil "#~%# the tag ID number for an RFID tag~%#~%Header header~%string rfidTag~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.secs: seconds (stamp_secs) since epoch~%# * stamp.nsecs: nanoseconds since stamp_secs~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%# 0: no frame~%# 1: global frame~%string frame_id~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Rfid>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:length (cl:slot-value msg 'rfidTag))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Rfid>))
  "Converts a ROS message object to a list"
  (cl:list 'Rfid
    (cl:cons ':header (header msg))
    (cl:cons ':rfidTag (rfidTag msg))
))
