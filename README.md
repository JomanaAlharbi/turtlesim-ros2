# مشروع TurtleSim - ROS2

مشروع بسيط لبرمجة حركة السلحفاة (Turtle) في محاكي TurtleSim، بالإضافة إلى نظام Publisher/Subscriber بسيط، باستخدام ROS2 Humble ولغة بايثون.

## وصف المشروع

يحتوي هذا المشروع على سكربتات بايثون تنجز مهمتين رئيسيتين:

1. التحكم في حركة السلحفاة داخل محاكي TurtleSim عن طريق نشر أوامر السرعة (Twist Messages) إلى موضوع (Topic) باسم /turtle1/cmd_vel.
2. تطبيق Publisher و Subscriber بسيط يرسل ويستقبل رسالة نصية مخصصة عبر موضوع (Topic) باسم my_topic.

## الملفات

### مهمة حركة السلحفاة

- `turtle_circle.py`: يجعل السلحفاة تتحرك في مسار دائري مستمر عن طريق إعطائها سرعة خطية وسرعة زاوية ثابتتين في نفس الوقت.

- `turtle_square.py`: يجعل السلحفاة ترسم شكل مربع عن طريق التحكم في مراحل الحركة (التحرك للأمام ثم الدوران 90 درجة) بشكل متكرر أربع مرات.

### مهمة Publisher و Subscriber

- `publisher_node.py`: عقدة (Node) تنشر رسالة نصية ("Turning ideas into robots") كل ثانية إلى موضوع باسم my_topic.

- `subscriber_node.py`: عقدة (Node) تشترك في موضوع my_topic وتطبع كل رسالة تستقبلها من الـ Publisher.

## المتطلبات

- نظام Ubuntu 22.04
- ROS2 Humble
- حزمة turtlesim
- بايثون 3

## طريقة التشغيل

### 1. تفعيل بيئة ROS2

    source /opt/ros/humble/setup.bash

### مهمة حركة السلحفاة

#### تشغيل محاكي TurtleSim (في نافذة تيرمنال أولى)

    ros2 run turtlesim turtlesim_node

#### تشغيل سكربت الحركة (في نافذة تيرمنال ثانية)

لتشغيل حركة الدائرة:

    python3 turtle_circle.py

لتشغيل حركة المربع:

    python3 turtle_square.py
### مهمة Publisher و Subscriber

#### تشغيل الـ Publisher (في نافذة تيرمنال أولى)

    python3 publisher_node.py

#### تشغيل الـ Subscriber (في نافذة تيرمنال ثانية)

    python3 subscriber_node.py

بعد تشغيل الملفين، ستظهر رسائل "Publishing" في نافذة الـ Publisher، ورسائل "I heard" في نافذة الـ Subscriber بنفس الوقت، مما يؤكد نجاح الاتصال بين العقدتين.

## ملاحظات

- سكربت turtle_square.py مصمم ليتوقف تلقائيًا بعد إكمال رسم مربع واحد بالكامل.
- يُنصح بعمل reset قبل كل تشغيل جديد لضمان الحصول على شكل نظيف وواضح.
- يجب تشغيل الـ Publisher والـ Subscriber في نافذتي تيرمنال منفصلتين في نفس الوقت.

## الكاتب

