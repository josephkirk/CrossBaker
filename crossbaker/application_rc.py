# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Tue Oct 16 11:10:52 2018
#      by: The Resource Compiler for PySide2 (Qt v5.11.2)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
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
\x00\x00\x01f\
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
Material\x0d\x0aFont\x5cF\
amily=Open Sans\x0d\
\x0aFont\x5cPixelSize=\
20\x0d\x0a\x0d\x0a[Material]\
\x0d\x0aTheme=Dark\x0d\x0a;A\
ccent=Teal\x0d\x0a;Pri\
mary=BlueGray\x0d\x0a;\
Foreground=Brown\
\x0d\x0a;Background=Bl\
ack\x0d\x0a\
\x00\x00\x07\xb7\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Controls 2.4\x0d\
\x0a\x0d\x0aApplicationWi\
ndow {\x0d\x0a    id: \
window\x0d\x0a    visi\
ble: true\x0d\x0a    w\
idth: 400\x0d\x0a    h\
eight: 800\x0d\x0a    \
title: qsTr(\x22Cro\
ss Baker\x22)\x0d\x0a\x0d\x0a  \
  header: ToolBa\
r {\x0d\x0a        con\
tentHeight: tool\
Button.implicitH\
eight\x0d\x0a\x0d\x0a       \
 Label {\x0d\x0a      \
      id: toolhe\
ader\x0d\x0a          \
  text: \x22Main\x22\x0d\x0a\
            anch\
ors.verticalCent\
er: parent.verti\
calCenter\x0d\x0a     \
       anchors.l\
eft:parent.left\x0d\
\x0a            anc\
hors.leftMargin:\
 20\x0d\x0a        }\x0d\x0a\
\x0d\x0a        ToolBu\
tton {\x0d\x0a        \
    id: toolButt\
on\x0d\x0a            \
x: window.width-\
50\x0d\x0a            \
y: 0\x0d\x0a          \
  text: stackVie\
w.depth > 1 ? \x22\x5c\
u25C0\x22 : \x22\x5cu2630\
\x22\x0d\x0a            f\
ont.pixelSize: Q\
t.application.fo\
nt.pixelSize * 1\
.6\x0d\x0a            \
onClicked: {\x0d\x0a  \
              if\
 (stackView.dept\
h > 1) {\x0d\x0a      \
              st\
ackView.pop()\x0d\x0a \
                \
   toolheader.te\
xt = \x22Main\x22\x0d\x0a   \
             } e\
lse {\x0d\x0a         \
           drawe\
r.open()\x0d\x0a      \
          }\x0d\x0a   \
         }\x0d\x0a    \
    }\x0d\x0a\x0d\x0a\x0d\x0a    }\
\x0d\x0a\x0d\x0a    Drawer {\
\x0d\x0a        id: dr\
awer\x0d\x0a        wi\
dth: window.widt\
h * 0.66\x0d\x0a      \
  height: window\
.height\x0d\x0a\x0d\x0a     \
   Column {\x0d\x0a   \
         anchors\
.fill: parent\x0d\x0a\x0d\
\x0a            Ite\
mDelegate {\x0d\x0a   \
             tex\
t: qsTr(\x22Page 1\x22\
)\x0d\x0a             \
   width: parent\
.width\x0d\x0a        \
        onClicke\
d: {\x0d\x0a          \
          stackV\
iew.push(\x22Page1F\
orm.ui.qml\x22)\x0d\x0a  \
                \
  drawer.close()\
\x0d\x0a              \
      toolheader\
.text = \x22Page 1\x22\
\x0d\x0a              \
  }\x0d\x0a           \
 }\x0d\x0a            \
ItemDelegate {\x0d\x0a\
                \
text: qsTr(\x22Page\
 2\x22)\x0d\x0a          \
      width: par\
ent.width\x0d\x0a     \
           onCli\
cked: {\x0d\x0a       \
             sta\
ckView.push(\x22Pag\
e2Form.ui.qml\x22)\x0d\
\x0a               \
     drawer.clos\
e()\x0d\x0a           \
         toolhea\
der.text = \x22Page\
 2\x22\x0d\x0a           \
     }\x0d\x0a        \
    }\x0d\x0a        }\
\x0d\x0a    }\x0d\x0a\x0d\x0a    S\
tackView {\x0d\x0a    \
    id: stackVie\
w\x0d\x0a        initi\
alItem: \x22HomeFor\
m.ui.qml\x22\x0d\x0a     \
   anchors.fill:\
 parent\x0d\x0a       \
 width: window.w\
idth\x0d\x0a\x0d\x0a    }\x0d\x0a}\
\x0d\x0a\x0d\x0a/*##^## Desi\
gner {\x0d\x0a    D{i:\
0;height:800;wid\
th:400}\x0d\x0a}\x0d\x0a ##^\
##*/\x0d\x0a\
\x00\x00\x04%\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Controls 2.4\x0d\
\x0aimport QtQuick.\
Controls 1.4\x0d\x0aim\
port Qt.labs.fol\
derlistmodel 2.1\
1\x0d\x0aimport QtQml.\
Models 2.11\x0d\x0aPag\
e {\x0d\x0a    id: hom\
ePage\x0d\x0a    title\
: qsTr(\x22Home\x22)\x0d\x0a\
    width: 400\x0d\x0a\
    height: 800\x0d\
\x0a\x0d\x0a\x0d\x0a    ScrollV\
iew {\x0d\x0a        a\
nchors.fill: par\
ent\x0d\x0a        Col\
umn {\x0d\x0a         \
   spacing: 2\x0d\x0a \
           Label\
 {\x0d\x0a            \
    text: qsTr(\x22\
You are on the h\
ome page.\x22)\x0d\x0a   \
         }\x0d\x0a\x0d\x0a  \
          TreeVi\
ew {\x0d\x0a          \
      id: object\
view\x0d\x0a          \
      FolderList\
Model {\x0d\x0a       \
             id:\
 folderModel\x0d\x0a  \
                \
  nameFilters: [\
\x22*.obj\x22, \x22*.fbx\x22\
]\x0d\x0a             \
       rootFolde\
r: \x22D:/test/marm\
osetBaker\x22\x0d\x0a    \
                \
showDirs: true\x0d\x0a\
                \
    showDotAndDo\
tDot: true\x0d\x0a    \
            }\x0d\x0a \
               m\
odel: folderMode\
l\x0d\x0a             \
   selection: It\
emSelectionModel\
 {\x0d\x0a            \
        model: f\
olderModel\x0d\x0a    \
            }\x0d\x0a \
               T\
ableViewColumn {\
\x0d\x0a              \
      title: \x22Na\
me\x22\x0d\x0a           \
         role: \x22\
fileName\x22\x0d\x0a     \
           }\x0d\x0a\x0d\x0a\
            }\x0d\x0a \
       }\x0d\x0a    }\x0d\
\x0a}\x0d\x0a\
\x00\x00\x06\xe6\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Controls 2.4\x0d\
\x0a\x0d\x0aPage {\x0d\x0a    w\
idth: 400\x0d\x0a    h\
eight: 400\x0d\x0a\x0d\x0a  \
  title: qsTr(\x22P\
age 1\x22)\x0d\x0a\x0d\x0a    L\
abel {\x0d\x0a        \
text: qsTr(\x22You \
are on Page 1.\x22)\
\x0d\x0a        anchor\
s.centerIn: pare\
nt\x0d\x0a    }\x0d\x0a\x0d\x0a   \
 TextEdit {\x0d\x0a   \
     id: textEdi\
t\x0d\x0a        x: 12\
5\x0d\x0a        y: 90\
\x0d\x0a        width:\
 80\x0d\x0a        hei\
ght: 20\x0d\x0a       \
 text: qsTr(\x22Tex\
t Edit\x22)\x0d\x0a      \
  font.bold: tru\
e\x0d\x0a        font.\
family: \x22Courier\
\x22\x0d\x0a        horiz\
ontalAlignment: \
Text.AlignLeft\x0d\x0a\
        font.pix\
elSize: 12\x0d\x0a    \
}\x0d\x0a\x0d\x0a    CheckBo\
x {\x0d\x0a        id:\
 checkBox\x0d\x0a     \
   x: 9\x0d\x0a       \
 y: 398\x0d\x0a       \
 width: 196\x0d\x0a   \
     height: 32\x0d\
\x0a        text: q\
sTr(\x22Check Box\x22)\
\x0d\x0a    }\x0d\x0a\x0d\x0a    L\
istView {\x0d\x0a     \
   id: listView\x0d\
\x0a        x: 14\x0d\x0a\
        y: 112\x0d\x0a\
        width: 1\
91\x0d\x0a        heig\
ht: 242\x0d\x0a       \
 delegate: Item \
{\x0d\x0a            x\
: 5\x0d\x0a           \
 width: 80\x0d\x0a    \
        height: \
40\x0d\x0a            \
Row {\x0d\x0a         \
       id: row1\x0d\
\x0a               \
 spacing: 10\x0d\x0a  \
              Re\
ctangle {\x0d\x0a     \
               w\
idth: 40\x0d\x0a      \
              he\
ight: 40\x0d\x0a      \
              co\
lor: colorCode\x0d\x0a\
                \
}\x0d\x0a\x0d\x0a           \
     Text {\x0d\x0a   \
                \
 text: name\x0d\x0a   \
                \
 font.bold: true\
\x0d\x0a              \
      anchors.ve\
rticalCenter: pa\
rent.verticalCen\
ter\x0d\x0a           \
     }\x0d\x0a        \
    }\x0d\x0a        }\
\x0d\x0a        model:\
 ListModel {\x0d\x0a  \
          ListEl\
ement {\x0d\x0a       \
         name: \x22\
Grey\x22\x0d\x0a         \
       colorCode\
: \x22grey\x22\x0d\x0a      \
      }\x0d\x0a\x0d\x0a     \
       ListEleme\
nt {\x0d\x0a          \
      name: \x22Red\
\x22\x0d\x0a             \
   colorCode: \x22r\
ed\x22\x0d\x0a           \
 }\x0d\x0a\x0d\x0a          \
  ListElement {\x0d\
\x0a               \
 name: \x22Blue\x22\x0d\x0a \
               c\
olorCode: \x22blue\x22\
\x0d\x0a            }\x0d\
\x0a\x0d\x0a            L\
istElement {\x0d\x0a  \
              na\
me: \x22Green\x22\x0d\x0a   \
             col\
orCode: \x22green\x22\x0d\
\x0a            }\x0d\x0a\
        }\x0d\x0a    }\
\x0d\x0a}\x0d\x0a\
"

qt_resource_name = b"\
\x00\x10\
\x05w\x1a\xdc\
\x00P\
\x00a\x00g\x00e\x002\x00F\x00o\x00r\x00m\x00.\x00u\x00i\x00.\x00q\x00m\x00l\
\x00\x15\
\x08\x1e\x16f\
\x00q\
\x00t\x00q\x00u\x00i\x00c\x00k\x00c\x00o\x00n\x00t\x00r\x00o\x00l\x00s\x002\x00.\
\x00c\x00o\x00n\x00f\
\x00\x08\
\x08\x01Z\x5c\
\x00m\
\x00a\x00i\x00n\x00.\x00q\x00m\x00l\
\x00\x0f\
\x02\x83\xbc\xbc\
\x00H\
\x00o\x00m\x00e\x00F\x00o\x00r\x00m\x00.\x00u\x00i\x00.\x00q\x00m\x00l\
\x00\x10\
\x05\x17\x1a\xdc\
\x00P\
\x00a\x00g\x00e\x001\x00F\x00o\x00r\x00m\x00.\x00u\x00i\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00\x01\
\x00\x00\x00l\x00\x00\x00\x00\x00\x01\x00\x00\x0a\x08\
\x00\x00\x00\x90\x00\x00\x00\x00\x00\x01\x00\x00\x0e1\
\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00V\x00\x00\x00\x00\x00\x01\x00\x00\x02M\
\x00\x00\x00&\x00\x00\x00\x00\x00\x01\x00\x00\x00\xe3\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
