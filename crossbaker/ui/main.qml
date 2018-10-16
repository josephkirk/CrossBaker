import QtQuick 2.11
import QtQuick.Controls 2.4

ApplicationWindow {
    id: window
    visible: true
    width: 400
    height: 800
    title: qsTr("Cross Baker")

    header: ToolBar {
        contentHeight: toolButton.implicitHeight

        Label {
            id: toolheader
            text: "Main"
            anchors.verticalCenter: parent.verticalCenter
            anchors.left:parent.left
            anchors.leftMargin: 20
        }

        ToolButton {
            id: toolButton
            x: window.width-50
            y: 0
            text: stackView.depth > 1 ? "\u25C0" : "\u2630"
            font.pixelSize: Qt.application.font.pixelSize * 1.6
            onClicked: {
                if (stackView.depth > 1) {
                    stackView.pop()
                    toolheader.text = "Main"
                } else {
                    drawer.open()
                }
            }
        }


    }

    Drawer {
        id: drawer
        width: window.width * 0.66
        height: window.height

        Column {
            anchors.fill: parent

            ItemDelegate {
                text: qsTr("Page 1")
                width: parent.width
                onClicked: {
                    stackView.push("Page1Form.ui.qml")
                    drawer.close()
                    toolheader.text = "Page 1"
                }
            }
            ItemDelegate {
                text: qsTr("Page 2")
                width: parent.width
                onClicked: {
                    stackView.push("Page2Form.ui.qml")
                    drawer.close()
                    toolheader.text = "Page 2"
                }
            }
        }
    }

    StackView {
        id: stackView
        initialItem: "HomeForm.ui.qml"
        anchors.fill: parent
        width: window.width

    }
}

/*##^## Designer {
    D{i:0;height:800;width:400}
}
 ##^##*/
