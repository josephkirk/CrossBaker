# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Tue Oct 16 00:17:57 2018
#      by: The Resource Compiler for PySide2 (Qt v5.11.2)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xe4\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Controls 2.4\x0d\
\x0a\x0d\x0aPage {\x0d\x0a    w\
idth: 600\x0d\x0a    h\
eight: 400\x0d\x0a\x0d\x0a  \
  title: qsTr(\x22H\
ome\x22)\x0d\x0a\x0d\x0a    Lab\
el {\x0d\x0a        te\
xt: qsTr(\x22You ar\
e on the home pa\
ge.\x22)\x0d\x0a        a\
nchors.centerIn:\
 parent\x0d\x0a    }\x0d\x0a\
}\x0d\x0a\
\x00\x00\x00\xdf\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Controls 2.4\x0d\
\x0a\x0d\x0aPage {\x0d\x0a    w\
idth: 600\x0d\x0a    h\
eight: 400\x0d\x0a\x0d\x0a  \
  title: qsTr(\x22P\
age 2\x22)\x0d\x0a\x0d\x0a    L\
abel {\x0d\x0a        \
text: qsTr(\x22You \
are on Page 2.\x22)\
\x0d\x0a        anchor\
s.centerIn: pare\
nt\x0d\x0a    }\x0d\x0a}\x0d\x0a\
\x00\x00\x0d\xfe\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Controls 2.4\x0d\
\x0a\x0d\x0aApplicationWi\
ndow {\x0d\x0a    id: \
window\x0d\x0a    visi\
ble: true\x0d\x0a    w\
idth: 640\x0d\x0a    h\
eight: 480\x0d\x0a    \
title: qsTr(\x22Cro\
ss Baker\x22)\x0d\x0a\x0d\x0a  \
  header: ToolBa\
r {\x0d\x0a        con\
tentHeight: tool\
Button.implicitH\
eight\x0d\x0a\x0d\x0a       \
 ToolButton {\x0d\x0a \
           id: t\
oolButton\x0d\x0a     \
       x: 359\x0d\x0a \
           y: 0\x0d\
\x0a            tex\
t: stackView.dep\
th > 1 ? \x22\x5cu25C0\
\x22 : \x22\x5cu2630\x22\x0d\x0a  \
          font.p\
ixelSize: Qt.app\
lication.font.pi\
xelSize * 1.6\x0d\x0a \
           onCli\
cked: {\x0d\x0a       \
         if (sta\
ckView.depth > 1\
) {\x0d\x0a           \
         stackVi\
ew.pop()\x0d\x0a      \
          } else\
 {\x0d\x0a            \
        drawer.o\
pen()\x0d\x0a         \
       }\x0d\x0a      \
      }\x0d\x0a       \
 }\x0d\x0a\x0d\x0a        La\
bel {\x0d\x0a         \
   text: \x22#stack\
View.currentItem\
.title#\x22\x0d\x0a      \
      anchors.ve\
rticalCenterOffs\
et: -27\x0d\x0a       \
     anchors.hor\
izontalCenterOff\
set: 75\x0d\x0a       \
     anchors.cen\
terIn: parent\x0d\x0a \
       }\x0d\x0a    }\x0d\
\x0a\x0d\x0a    Drawer {\x0d\
\x0a        id: dra\
wer\x0d\x0a        wid\
th: window.width\
 * 0.66\x0d\x0a       \
 height: window.\
height\x0d\x0a\x0d\x0a      \
  Column {\x0d\x0a    \
        anchors.\
fill: parent\x0d\x0a\x0d\x0a\
            Item\
Delegate {\x0d\x0a    \
            text\
: qsTr(\x22Page 1\x22)\
\x0d\x0a              \
  width: parent.\
width\x0d\x0a         \
       onClicked\
: {\x0d\x0a           \
         stackVi\
ew.push(\x22Page1Fo\
rm.ui.qml\x22)\x0d\x0a   \
                \
 drawer.close()\x0d\
\x0a               \
 }\x0d\x0a            \
}\x0d\x0a            I\
temDelegate {\x0d\x0a \
               t\
ext: qsTr(\x22Page \
2\x22)\x0d\x0a           \
     width: pare\
nt.width\x0d\x0a      \
          onClic\
ked: {\x0d\x0a        \
            stac\
kView.push(\x22Page\
2Form.ui.qml\x22)\x0d\x0a\
                \
    drawer.close\
()\x0d\x0a            \
    }\x0d\x0a         \
   }\x0d\x0a        }\x0d\
\x0a    }\x0d\x0a\x0d\x0a    St\
ackView {\x0d\x0a     \
   id: stackView\
\x0d\x0a        initia\
lItem: \x22HomeForm\
.ui.qml\x22\x0d\x0a      \
  anchors.fill: \
parent\x0d\x0a\x0d\x0a      \
  TextEdit {\x0d\x0a  \
          id: te\
xtEdit\x0d\x0a        \
    x: 125\x0d\x0a    \
        y: 90\x0d\x0a \
           width\
: 80\x0d\x0a          \
  height: 20\x0d\x0a  \
          text: \
qsTr(\x22Text Edit\x22\
)\x0d\x0a            f\
ont.bold: true\x0d\x0a\
            font\
.family: \x22Courie\
r\x22\x0d\x0a            \
horizontalAlignm\
ent: Text.AlignL\
eft\x0d\x0a           \
 font.pixelSize:\
 12\x0d\x0a        }\x0d\x0a\
\x0d\x0a        CheckB\
ox {\x0d\x0a          \
  id: checkBox\x0d\x0a\
            x: 9\
\x0d\x0a            y:\
 398\x0d\x0a          \
  width: 196\x0d\x0a  \
          height\
: 32\x0d\x0a          \
  text: qsTr(\x22Ch\
eck Box\x22)\x0d\x0a     \
   }\x0d\x0a\x0d\x0a        \
ListView {\x0d\x0a    \
        id: list\
View\x0d\x0a          \
  x: 14\x0d\x0a       \
     y: 112\x0d\x0a   \
         width: \
191\x0d\x0a           \
 height: 242\x0d\x0a  \
          delega\
te: Item {\x0d\x0a    \
            x: 5\
\x0d\x0a              \
  width: 80\x0d\x0a   \
             hei\
ght: 40\x0d\x0a       \
         Row {\x0d\x0a\
                \
    id: row1\x0d\x0a  \
                \
  spacing: 10\x0d\x0a \
                \
   Rectangle {\x0d\x0a\
                \
        width: 4\
0\x0d\x0a             \
           heigh\
t: 40\x0d\x0a         \
               c\
olor: colorCode\x0d\
\x0a               \
     }\x0d\x0a\x0d\x0a      \
              Te\
xt {\x0d\x0a          \
              te\
xt: name\x0d\x0a      \
                \
  font.bold: tru\
e\x0d\x0a             \
           ancho\
rs.verticalCente\
r: parent.vertic\
alCenter\x0d\x0a      \
              }\x0d\
\x0a               \
 }\x0d\x0a            \
}\x0d\x0a            m\
odel: ListModel \
{\x0d\x0a             \
   ListElement {\
\x0d\x0a              \
      name: \x22Gre\
y\x22\x0d\x0a            \
        colorCod\
e: \x22grey\x22\x0d\x0a     \
           }\x0d\x0a\x0d\x0a\
                \
ListElement {\x0d\x0a \
                \
   name: \x22Red\x22\x0d\x0a\
                \
    colorCode: \x22\
red\x22\x0d\x0a          \
      }\x0d\x0a\x0d\x0a     \
           ListE\
lement {\x0d\x0a      \
              na\
me: \x22Blue\x22\x0d\x0a    \
                \
colorCode: \x22blue\
\x22\x0d\x0a             \
   }\x0d\x0a\x0d\x0a        \
        ListElem\
ent {\x0d\x0a         \
           name:\
 \x22Green\x22\x0d\x0a      \
              co\
lorCode: \x22green\x22\
\x0d\x0a              \
  }\x0d\x0a           \
 }\x0d\x0a        }\x0d\x0a \
   }\x0d\x0a}\x0d\x0a\x0d\x0a/*##^\
## Designer {\x0d\x0a \
   D{i:0;height:\
800;width:400}\x0d\x0a\
}\x0d\x0a ##^##*/\x0d\x0a\
\x00\x00\x00\xdf\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Controls 2.4\x0d\
\x0a\x0d\x0aPage {\x0d\x0a    w\
idth: 600\x0d\x0a    h\
eight: 400\x0d\x0a\x0d\x0a  \
  title: qsTr(\x22P\
age 1\x22)\x0d\x0a\x0d\x0a    L\
abel {\x0d\x0a        \
text: qsTr(\x22You \
are on Page 1.\x22)\
\x0d\x0a        anchor\
s.centerIn: pare\
nt\x0d\x0a    }\x0d\x0a}\x0d\x0a\
\x00\x00\x01?\
;\
 This file can b\
e edited to chan\
ge the style of \
the application\x0d\
\x0a; Read \x22Qt Quic\
k Controls 2 Con\
figuration File\x22\
 for details:\x0d\x0a;\
 http://doc.qt.i\
o/qt-5/qtquickco\
ntrols2-configur\
ation.html\x0d\x0a\x0d\x0a[C\
ontrols]\x0d\x0aStyle=\
Material\x0d\x0a\x0d\x0a[Mat\
erial]\x0d\x0aTheme=Da\
rk\x0d\x0a;Accent=Blue\
Grey\x0d\x0a;Primary=B\
lueGray\x0d\x0a;Foregr\
ound=Brown\x0d\x0a;Bac\
kground=Grey\x0d\x0a\
"

qt_resource_name = b"\
\x00\x0f\
\x02\x83\xbc\xbc\
\x00H\
\x00o\x00m\x00e\x00F\x00o\x00r\x00m\x00.\x00u\x00i\x00.\x00q\x00m\x00l\
\x00\x10\
\x05w\x1a\xdc\
\x00P\
\x00a\x00g\x00e\x002\x00F\x00o\x00r\x00m\x00.\x00u\x00i\x00.\x00q\x00m\x00l\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x10\
\x05\x17\x1a\xdc\
\x00P\
\x00a\x00g\x00e\x001\x00F\x00o\x00r\x00m\x00.\x00u\x00i\x00.\x00q\x00m\x00l\
\x00\x15\
\x08\x1e\x16f\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\x00.\
\x00c\x00o\x00n\x00f\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00`\x00\x00\x00\x00\x00\x01\x00\x00\x0f\xcd\
\x00\x00\x00$\x00\x00\x00\x00\x00\x01\x00\x00\x00\xe8\
\x00\x00\x00J\x00\x00\x00\x00\x00\x01\x00\x00\x01\xcb\
\x00\x00\x00\x86\x00\x00\x00\x00\x00\x01\x00\x00\x10\xb0\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
