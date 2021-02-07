;; Auto-generated. Do not edit!


(when (boundp 'learn_action::TurtleMoveFeedback)
  (if (not (find-package "LEARN_ACTION"))
    (make-package "LEARN_ACTION"))
  (shadow 'TurtleMoveFeedback (find-package "LEARN_ACTION")))
(unless (find-package "LEARN_ACTION::TURTLEMOVEFEEDBACK")
  (make-package "LEARN_ACTION::TURTLEMOVEFEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude TurtleMoveFeedback.msg.html


(defclass learn_action::TurtleMoveFeedback
  :super ros::object
  :slots (_present_turtle_x _present_turtle_y _present_turtle_theta ))

(defmethod learn_action::TurtleMoveFeedback
  (:init
   (&key
    ((:present_turtle_x __present_turtle_x) 0.0)
    ((:present_turtle_y __present_turtle_y) 0.0)
    ((:present_turtle_theta __present_turtle_theta) 0.0)
    )
   (send-super :init)
   (setq _present_turtle_x (float __present_turtle_x))
   (setq _present_turtle_y (float __present_turtle_y))
   (setq _present_turtle_theta (float __present_turtle_theta))
   self)
  (:present_turtle_x
   (&optional __present_turtle_x)
   (if __present_turtle_x (setq _present_turtle_x __present_turtle_x)) _present_turtle_x)
  (:present_turtle_y
   (&optional __present_turtle_y)
   (if __present_turtle_y (setq _present_turtle_y __present_turtle_y)) _present_turtle_y)
  (:present_turtle_theta
   (&optional __present_turtle_theta)
   (if __present_turtle_theta (setq _present_turtle_theta __present_turtle_theta)) _present_turtle_theta)
  (:serialization-length
   ()
   (+
    ;; float64 _present_turtle_x
    8
    ;; float64 _present_turtle_y
    8
    ;; float64 _present_turtle_theta
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _present_turtle_x
       (sys::poke _present_turtle_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _present_turtle_y
       (sys::poke _present_turtle_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _present_turtle_theta
       (sys::poke _present_turtle_theta (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _present_turtle_x
     (setq _present_turtle_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _present_turtle_y
     (setq _present_turtle_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _present_turtle_theta
     (setq _present_turtle_theta (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get learn_action::TurtleMoveFeedback :md5sum-) "4d26027f0f230cc5b61fa6b93405965c")
(setf (get learn_action::TurtleMoveFeedback :datatype-) "learn_action/TurtleMoveFeedback")
(setf (get learn_action::TurtleMoveFeedback :definition-)
      "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Define a feedback message
float64 present_turtle_x
float64 present_turtle_y
float64 present_turtle_theta


")



(provide :learn_action/TurtleMoveFeedback "4d26027f0f230cc5b61fa6b93405965c")

