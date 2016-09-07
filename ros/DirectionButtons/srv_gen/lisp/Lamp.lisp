; Auto-generated. Do not edit!


(cl:in-package DirectionButtons-srv)


;//! \htmlinclude Lamp-request.msg.html

(cl:defclass <Lamp-request> (roslisp-msg-protocol:ros-message)
  ((lampStates
    :reader lampStates
    :initarg :lampStates
    :type cl:fixnum
    :initform 0))
)

(cl:defclass Lamp-request (<Lamp-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Lamp-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Lamp-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name DirectionButtons-srv:<Lamp-request> is deprecated: use DirectionButtons-srv:Lamp-request instead.")))

(cl:ensure-generic-function 'lampStates-val :lambda-list '(m))
(cl:defmethod lampStates-val ((m <Lamp-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader DirectionButtons-srv:lampStates-val is deprecated.  Use DirectionButtons-srv:lampStates instead.")
  (lampStates m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Lamp-request>) ostream)
  "Serializes a message object of type '<Lamp-request>"
  (cl:let* ((signed (cl:slot-value msg 'lampStates)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Lamp-request>) istream)
  "Deserializes a message object of type '<Lamp-request>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'lampStates) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Lamp-request>)))
  "Returns string type for a service object of type '<Lamp-request>"
  "DirectionButtons/LampRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Lamp-request)))
  "Returns string type for a service object of type 'Lamp-request"
  "DirectionButtons/LampRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Lamp-request>)))
  "Returns md5sum for a message object of type '<Lamp-request>"
  "72b2d4e139920609dcfb8d877267a3c7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Lamp-request)))
  "Returns md5sum for a message object of type 'Lamp-request"
  "72b2d4e139920609dcfb8d877267a3c7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Lamp-request>)))
  "Returns full string definition for message of type '<Lamp-request>"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%int8 lampStates~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Lamp-request)))
  "Returns full string definition for message of type 'Lamp-request"
  (cl:format cl:nil "~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%int8 lampStates~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Lamp-request>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Lamp-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Lamp-request
    (cl:cons ':lampStates (lampStates msg))
))
;//! \htmlinclude Lamp-response.msg.html

(cl:defclass <Lamp-response> (roslisp-msg-protocol:ros-message)
  ((succeeded
    :reader succeeded
    :initarg :succeeded
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass Lamp-response (<Lamp-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Lamp-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Lamp-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name DirectionButtons-srv:<Lamp-response> is deprecated: use DirectionButtons-srv:Lamp-response instead.")))

(cl:ensure-generic-function 'succeeded-val :lambda-list '(m))
(cl:defmethod succeeded-val ((m <Lamp-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader DirectionButtons-srv:succeeded-val is deprecated.  Use DirectionButtons-srv:succeeded instead.")
  (succeeded m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Lamp-response>) ostream)
  "Serializes a message object of type '<Lamp-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'succeeded) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Lamp-response>) istream)
  "Deserializes a message object of type '<Lamp-response>"
    (cl:setf (cl:slot-value msg 'succeeded) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Lamp-response>)))
  "Returns string type for a service object of type '<Lamp-response>"
  "DirectionButtons/LampResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Lamp-response)))
  "Returns string type for a service object of type 'Lamp-response"
  "DirectionButtons/LampResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Lamp-response>)))
  "Returns md5sum for a message object of type '<Lamp-response>"
  "72b2d4e139920609dcfb8d877267a3c7")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Lamp-response)))
  "Returns md5sum for a message object of type 'Lamp-response"
  "72b2d4e139920609dcfb8d877267a3c7")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Lamp-response>)))
  "Returns full string definition for message of type '<Lamp-response>"
  (cl:format cl:nil "~%~%~%bool succeeded~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Lamp-response)))
  "Returns full string definition for message of type 'Lamp-response"
  (cl:format cl:nil "~%~%~%bool succeeded~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Lamp-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Lamp-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Lamp-response
    (cl:cons ':succeeded (succeeded msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Lamp)))
  'Lamp-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Lamp)))
  'Lamp-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Lamp)))
  "Returns string type for a service object of type '<Lamp>"
  "DirectionButtons/Lamp")
