# -*- coding: utf-8 -*-

# Resource object code
#
# Created: Thu Dec 27 14:54:34 2018
#      by: The Resource Compiler for PySide2 (Qt v5.12.0)
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore

qt_resource_data = b"\
\x00\x00\x01b\
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
\x0aFont\x5cPointSize=\
20\x0d\x0a\x0d\x0a[Material]\
\x0d\x0aTheme=Dark\x0d\x0aAc\
cent=Teal\x0d\x0aPrima\
ry=BlueGray\x0d\x0aFor\
eground=Brown\x0d\x0aB\
ackground=Black\x0d\
\x0a\
\x00\x00\x08\xef\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Controls 2.4\x0d\
\x0aApplicationWind\
ow {\x0d\x0a    id: wi\
ndow\x0d\x0a    // fla\
gs: Qt.Window\x0d\x0a \
   // objectname\
: \x22mainwindow\x22\x0d\x0a\
    title: qsTr(\
\x22Cross Baker\x22)\x0d\x0a\
    visible: tru\
e\x0d\x0a    // active\
: true\x0d\x0a    // f\
lags: Qt.Window\x0d\
\x0a    width: 400\x0d\
\x0a    height: 800\
\x0d\x0a    maximumWid\
th: 400\x0d\x0a    max\
imumHeight: 800\x0d\
\x0a    minimumWidt\
h: 200\x0d\x0a    mini\
mumHeight: 400\x0d\x0a\
\x0d\x0a    header: To\
olBar {\x0d\x0a       \
 contentHeight: \
toolButton.impli\
citHeight\x0d\x0a\x0d\x0a   \
     Label {\x0d\x0a  \
          id: to\
olheader\x0d\x0a      \
      text: \x22SET\
UP\x22\x0d\x0a           \
 anchors.vertica\
lCenter: parent.\
verticalCenter\x0d\x0a\
            anch\
ors.left:parent.\
left\x0d\x0a          \
  anchors.leftMa\
rgin: 20\x0d\x0a      \
  }\x0d\x0a\x0d\x0a        T\
oolButton {\x0d\x0a   \
         id: too\
lButton\x0d\x0a       \
     x: window.w\
idth-50\x0d\x0a       \
     y: 0\x0d\x0a     \
       text: sta\
ckView.depth > 1\
 ? \x22\x5cu25C0\x22 : \x22\x5c\
u2630\x22\x0d\x0a        \
    font.pixelSi\
ze: Qt.applicati\
on.font.pixelSiz\
e * 1.6\x0d\x0a       \
     onClicked: \
{\x0d\x0a             \
   if (stackView\
.depth > 1) {\x0d\x0a \
                \
   stackView.pop\
()\x0d\x0a            \
        toolhead\
er.text = \x22SETUP\
\x22\x0d\x0a             \
   } else {\x0d\x0a   \
                \
 drawer.open()\x0d\x0a\
                \
}\x0d\x0a            }\
\x0d\x0a        }\x0d\x0a\x0d\x0a\x0d\
\x0a    }\x0d\x0a\x0d\x0a    Dr\
awer {\x0d\x0a        \
id: drawer\x0d\x0a    \
    width: windo\
w.width * 0.66\x0d\x0a\
        height: \
window.height\x0d\x0a \
       // intera\
ctive: false\x0d\x0a  \
      Column {\x0d\x0a\
            anch\
ors.fill: parent\
\x0d\x0a\x0d\x0a            \
ItemDelegate {\x0d\x0a\
                \
text: qsTr(\x22SETT\
INGS\x22)\x0d\x0a        \
        width: p\
arent.width\x0d\x0a   \
             onC\
licked: {\x0d\x0a     \
               s\
tackView.push(\x22f\
orms/SettingForm\
.qml\x22)\x0d\x0a        \
            draw\
er.close()\x0d\x0a    \
                \
toolheader.text \
= \x22SETTINGS\x22\x0d\x0a  \
              }\x0d\
\x0a            }\x0d\x0a\
            Item\
Delegate {\x0d\x0a    \
            text\
: qsTr(\x22CONFIGS\x22\
)\x0d\x0a             \
   width: parent\
.width\x0d\x0a        \
        onClicke\
d: {\x0d\x0a          \
          stackV\
iew.push(\x22forms/\
ConfigsForm.qml\x22\
, {appconfigs:ap\
pconfigsmodel, b\
aker:baker})\x0d\x0a  \
                \
  drawer.close()\
\x0d\x0a              \
      toolheader\
.text = \x22CONFIGS\
\x22\x0d\x0a             \
   }\x0d\x0a          \
  }\x0d\x0a        }\x0d\x0a\
    }\x0d\x0a\x0d\x0a    Sta\
ckView {\x0d\x0a      \
  id: stackView\x0d\
\x0a        anchors\
.fill: parent\x0d\x0a \
       Component\
.onCompleted: {\x0d\
\x0a            sta\
ckView.push(\x0d\x0a  \
              \x22f\
orms/HomeForm.qm\
l\x22, {model:asset\
Model, baker:bak\
er, bakers:baker\
s})\x0d\x0a        }\x0d\x0a\
\x0d\x0a    }\x0d\x0a}\x0d\x0a\x0d\x0a\
\x00\x00\x07\xe5\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Controls 2.4\x0d\
\x0aimport \x22items\x22\x0d\
\x0aimport \x22delegat\
es\x22\x0d\x0aPage {\x0d\x0a   \
 id: configpage\x0d\
\x0a    title: qsTr\
(\x22Setting\x22)\x0d\x0a   \
 width: 400\x0d\x0a   \
 height: 750\x0d\x0a  \
  property var s\
ettings: undefin\
ed\x0d\x0a\x0d\x0a    header\
: PageHeader {\x0d\x0a\
        Row {\x0d\x0a \
           ancho\
rs.horizontalCen\
ter: parent.hori\
zontalCenter\x0d\x0a  \
          anchor\
s.verticalCenter\
: parent.vertica\
lCenter \x0d\x0a      \
      Text {\x0d\x0a  \
              te\
xt: qsTr(\x22Bake S\
etting\x22)\x0d\x0a      \
          font.p\
ixelSize: 24\x0d\x0a  \
              co\
lor: \x22white\x22\x0d\x0a  \
          }\x0d\x0a   \
     }\x0d\x0a    }\x0d\x0a\x0d\
\x0a    // Body\x0d\x0a  \
  PageBody {\x0d\x0a  \
      ListView {\
\x0d\x0a            x:\
 5; y: 10\x0d\x0a     \
       width: 60\
0; height: 600\x0d\x0a\
            spac\
ing: 5\x0d\x0a        \
    delegate: Ap\
pConfigDelegate \
{\x0d\x0a             \
   textColor:\x22bl\
ack\x22\x0d\x0a          \
      width: 600\
\x0d\x0a            }\x0d\
\x0a            pop\
ulate: Transitio\
n {\x0d\x0a           \
     SequentialA\
nimation {\x0d\x0a    \
                \
id: popTrans\x0d\x0a  \
                \
  PauseAnimation\
 {\x0d\x0a            \
            dura\
tion: (popTrans.\
ViewTransition.t\
argetIndexes * 2\
0)\x0d\x0a            \
            }\x0d\x0a \
                \
       NumberAni\
mation { propert\
y: \x22opacity\x22; fr\
om: 0; to: 1.0; \
duration: 150 }\x0d\
\x0a               \
         NumberA\
nimation { \x0d\x0a   \
                \
         propert\
ies: \x22y\x22; durati\
on: 150;\x0d\x0a      \
                \
      easing.typ\
e: Easing.InOutQ\
uad; }\x0d\x0a        \
            }\x0d\x0a \
           }\x0d\x0a\x0d\x0a\
            Comp\
onent.onComplete\
d: {\x0d\x0a          \
      // Delay l\
oad model for an\
imation\x0d\x0a       \
         if (set\
tings != undefin\
ed) {\x0d\x0a         \
           model\
 = settings\x0d\x0a   \
             }\x0d\x0a\
            }\x0d\x0a \
       }\x0d\x0a    }\x0d\
\x0a\x0d\x0a    footer: P\
ageFooter {\x0d\x0a   \
     Row {\x0d\x0a    \
        spacing:\
 10\x0d\x0a           \
 anchors.horizon\
talCenter: paren\
t.horizontalCent\
er\x0d\x0a            \
anchors.vertical\
Center: parent.v\
erticalCenter   \
   \x0d\x0a           \
 Button {\x0d\x0a     \
           width\
: 150\x0d\x0a         \
       text: \x22Sa\
ve Settings\x22\x0d\x0a  \
              on\
Clicked: {\x0d\x0a    \
                \
console.log(Sett\
ings)\x0d\x0a         \
       }\x0d\x0a      \
      }\x0d\x0a       \
 }\x0d\x0a    }\x0d\x0a    /\
/ Styling\x0d\x0a    \x0d\
\x0a}\x0d\x0a\
\x00\x00\x07\xe9\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Controls 2.4\x0d\
\x0aimport QtQml.Mo\
dels 2.11\x0d\x0aimpor\
t \x22delegates\x22\x0d\x0ai\
mport \x22stylings\x22\
\x0d\x0aimport \x22items\x22\
\x0d\x0aPage {\x0d\x0a    id\
: configpage\x0d\x0a  \
  title: qsTr(\x22C\
onfig\x22)\x0d\x0a    wid\
th: 400\x0d\x0a    hei\
ght: 750\x0d\x0a    pr\
operty var appco\
nfigs\x0d\x0a    prope\
rty var baker\x0d\x0a \
   header: PageH\
eader {\x0d\x0a       \
 Row {\x0d\x0a        \
    anchors.hori\
zontalCenter: pa\
rent.horizontalC\
enter\x0d\x0a         \
   anchors.verti\
calCenter: paren\
t.verticalCenter\
 \x0d\x0a            T\
ext {\x0d\x0a         \
       text: qsT\
r(\x22Application P\
ath\x22)\x0d\x0a         \
       font.pixe\
lSize: 24\x0d\x0a     \
           color\
: \x22white\x22\x0d\x0a     \
       }\x0d\x0a      \
  }\x0d\x0a    }\x0d\x0a\x0d\x0a  \
  // Body\x0d\x0a    P\
ageBody {\x0d\x0a     \
   ListView {\x0d\x0a \
           x: 5;\
 y: 10\x0d\x0a        \
    width: 600; \
height: 600\x0d\x0a   \
         spacing\
: 5\x0d\x0a           \
 delegate: AppCo\
nfigDelegate {\x0d\x0a\
                \
textColor:\x22black\
\x22\x0d\x0a             \
   width: 600\x0d\x0a \
           }\x0d\x0a  \
          popula\
te: Transition {\
\x0d\x0a              \
  SequentialAnim\
ation {\x0d\x0a       \
             id:\
 popTrans\x0d\x0a     \
               P\
auseAnimation {\x0d\
\x0a               \
         duratio\
n: (popTrans.Vie\
wTransition.targ\
etIndexes * 20)\x0d\
\x0a               \
         }\x0d\x0a    \
                \
    NumberAnimat\
ion { property: \
\x22opacity\x22; from:\
 0; to: 1.0; dur\
ation: 150 }\x0d\x0a  \
                \
      NumberAnim\
ation { \x0d\x0a      \
                \
      properties\
: \x22y\x22; duration:\
 150;\x0d\x0a         \
                \
   easing.type: \
Easing.InOutQuad\
; }\x0d\x0a           \
         }\x0d\x0a    \
        }\x0d\x0a\x0d\x0a   \
         Compone\
nt.onCompleted: \
{\x0d\x0a             \
   // Delay load\
 model for anima\
tion\x0d\x0a          \
      model = ap\
pconfigs\x0d\x0a      \
      }\x0d\x0a       \
 }\x0d\x0a    }\x0d\x0a\x0d\x0a   \
 footer: PageFoo\
ter {\x0d\x0a        R\
ow {\x0d\x0a          \
  spacing: 10\x0d\x0a \
           ancho\
rs.horizontalCen\
ter: parent.hori\
zontalCenter\x0d\x0a  \
          anchor\
s.verticalCenter\
: parent.vertica\
lCenter      \x0d\x0a \
           Butto\
n {\x0d\x0a           \
     width: 150\x0d\
\x0a               \
 text: \x22Save Con\
figs\x22\x0d\x0a         \
       onClicked\
: {\x0d\x0a           \
         console\
.log(baker.allAp\
psInfo())\x0d\x0a     \
           }\x0d\x0a  \
          }\x0d\x0a   \
     }\x0d\x0a    }\x0d\x0a \
   // Styling\x0d\x0a \
   \x0d\x0a}\x0d\x0a\
\x00\x00\x09\xad\
i\
mport QtQuick 2.\
11\x0d\x0aimport QtQui\
ck.Controls 2.4\x0d\
\x0aimport QtQml.Mo\
dels 2.11\x0d\x0aimpor\
t QtQuick.Layout\
s 1.11\x0d\x0aimport \x22\
stylings\x22\x0d\x0aimpor\
t \x22items\x22\x0d\x0aPage \
{\x0d\x0a    id: homep\
age\x0d\x0a    title: \
qsTr(\x22Set up\x22)\x0d\x0a\
    width: 400\x0d\x0a\
    height: 750\x0d\
\x0a    property va\
r model\x0d\x0a    pro\
perty var baker\x0d\
\x0a    property va\
r bakers\x0d\x0a    //\
 Components Init\
\x0d\x0a    BannerColo\
rs {\x0d\x0a        id\
: clubcolors\x0d\x0a  \
  }\x0d\x0a    header:\
 PageHeader {\x0d\x0a \
       Row {\x0d\x0a  \
          anchor\
s.horizontalCent\
er: parent.horiz\
ontalCenter\x0d\x0a   \
         anchors\
.verticalCenter:\
 parent.vertical\
Center \x0d\x0a       \
     Text {\x0d\x0a   \
             col\
or: \x22white\x22\x0d\x0a   \
             fon\
t.bold: true\x0d\x0a  \
              fo\
nt.pixelSize: 20\
\x0d\x0a              \
  text: \x22Baking \
Group\x22\x0d\x0a        \
    }\x0d\x0a        }\
\x0d\x0a    }\x0d\x0a\x0d\x0a    /\
/ Body\x0d\x0a    Dele\
gateModel {\x0d\x0a   \
     id: visualM\
odel\x0d\x0a        mo\
del: ListModel {\
\x0d\x0a            Li\
stElement { name\
: \x22Bake Group 1\x22\
 }\x0d\x0a            \
ListElement { na\
me: \x22Bake Group \
2\x22 }\x0d\x0a        }\x0d\
\x0a        delegat\
e: Rectangle {\x0d\x0a\
            heig\
ht: 50\x0d\x0a        \
    width: paren\
t.width-20\x0d\x0a    \
        color: \x22\
#3F5866\x22\x0d\x0a      \
      x: 10\x0d\x0a   \
         radius:\
 5\x0d\x0a            \
Row {\x0d\x0a         \
       anchors.v\
erticalCenter: p\
arent.verticalCe\
nter \x0d\x0a         \
       spacing: \
10\x0d\x0a            \
    padding: 10\x0d\
\x0a               \
 Rectangle {\x0d\x0a  \
                \
  radius: 5\x0d\x0a   \
                \
 width: 40\x0d\x0a    \
                \
height: 40\x0d\x0a    \
                \
color: \x22#BDD3DE\x22\
\x0d\x0a              \
  }\x0d\x0a           \
     Text { \x0d\x0a  \
                \
  color: \x22black\x22\
\x0d\x0a              \
      anchors.ve\
rticalCenter: pa\
rent.verticalCen\
ter\x0d\x0a           \
         text: n\
ame\x0d\x0a           \
         font.pi\
xelSize: 14\x0d\x0a   \
             }\x0d\x0a\
            }\x0d\x0a \
       }\x0d\x0a    }\x0d\
\x0a\x0d\x0a    PageBody \
{\x0d\x0a        ListV\
iew {\x0d\x0a         \
   x: 5; y: 10\x0d\x0a\
            widt\
h: parent.width;\
 height: 600\x0d\x0a  \
          spacin\
g: 5\x0d\x0a          \
  Component.onCo\
mpleted: {\x0d\x0a    \
            mode\
l = visualModel\x0d\
\x0a               \
 // console.log(\
layerModel)\x0d\x0a   \
         }\x0d\x0a    \
    }\x0d\x0a    }\x0d\x0a\x0d\x0a\
    footer: Page\
Footer {\x0d\x0a      \
  Row {\x0d\x0a       \
     spacing: 10\
\x0d\x0a            an\
chors.horizontal\
Center: parent.h\
orizontalCenter\x0d\
\x0a            anc\
hors.verticalCen\
ter: parent.vert\
icalCenter      \
     \x0d\x0a         \
   ComboBox {\x0d\x0a \
               /\
/ anchors.vertic\
alCenter: parent\
.verticalCenter\x0d\
\x0a               \
 width: 200\x0d\x0a   \
             mod\
el: bakers\x0d\x0a    \
        }\x0d\x0a     \
       Button {\x0d\
\x0a               \
 width: 150\x0d\x0a   \
             tex\
t: \x22Run Baker\x22\x0d\x0a\
                \
onClicked: baker\
.run()\x0d\x0a        \
    }\x0d\x0a        }\
\x0d\x0a    }\x0d\x0a}\x0d\x0a\
"

qt_resource_name = b"\
\x00\x02\
\x00\x00\x07\xb9\
\x00u\
\x00i\
\x00\x05\
\x00miC\
\x00f\
\x00o\x00r\x00m\x00s\
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
\x01\xf1\xa8\xbc\
\x00S\
\x00e\x00t\x00t\x00i\x00n\x00g\x00F\x00o\x00r\x00m\x00.\x00q\x00m\x00l\
\x00\x0f\
\x0f\x12\xb2\x1c\
\x00C\
\x00o\x00n\x00f\x00i\x00g\x00s\x00F\x00o\x00r\x00m\x00.\x00q\x00m\x00l\
\x00\x0c\
\x0fd'\x9c\
\x00H\
\x00o\x00m\x00e\x00F\x00o\x00r\x00m\x00.\x00q\x00m\x00l\
"

qt_resource_struct = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x02\
\x00\x00\x00\x0a\x00\x02\x00\x00\x00\x03\x00\x00\x00\x05\
\x00\x00\x00J\x00\x00\x00\x00\x00\x01\x00\x00\x01f\
\x00\x00\x00\x1a\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x00`\x00\x00\x00\x00\x00\x01\x00\x00\x0aY\
\x00\x00\x00\x84\x00\x00\x00\x00\x00\x01\x00\x00\x12B\
\x00\x00\x00\xa8\x00\x00\x00\x00\x00\x01\x00\x00\x1a/\
"

def qInitResources():
    QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
