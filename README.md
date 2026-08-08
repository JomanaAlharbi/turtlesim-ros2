مشروع TurtleSim - ROS2
مشروع بسيط لبرمجة حركة السلحفاة (Turtle) في محاكي TurtleSim باستخدام ROS2 Humble ولغة بايثون.
وصف المشروع
يحتوي هذا المشروع على سكربتات بايثون تتحكم في حركة السلحفاة داخل محاكي TurtleSim عن طريق نشر أوامر السرعة (Twist Messages) إلى موضوع (Topic) باسم /turtle1/cmd_vel.
الملفات
 • turtle_circle.py: يجعل السلحفاة تتحرك في مسار دائري مستمر عن طريق إعطائها سرعة خطية وسرعة زاوية ثابتتين في نفس الوقت.
 • turtle_square.py: يجعل السلحفاة ترسم شكل مربع عن طريق التحكم في مراحل الحركة (التحرك للأمام ثم الدوران 90 درجة) بشكل متكرر أربع مرات.
المتطلبات
 • نظام Ubuntu 22.04
 • ROS2 Humble
 • حزمة turtlesim
 • بايثون 3
طريقة التشغيل
1. تفعيل بيئة ROS2
source /opt/ros/humble/setup.bash

2. تشغيل محاكي TurtleSim (في نافذة تيرمنال أولى)
ros2 run turtlesim turtlesim_node

3. تشغيل سكربت الحركة (في نافذة تيرمنال ثانية)
لتشغيل حركة الدائرة:
python3 turtle_circle.py

لتشغيل حركة المربع:
python3 turtle_square.py
