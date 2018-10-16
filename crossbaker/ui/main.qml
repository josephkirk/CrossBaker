import QtQuick 2.5
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
                text: qsTr("Setting")
                width: parent.width
                onClicked: {
                    stackView.push("SettingForm.ui.qml")
                    drawer.close()
                    toolheader.text = "Setting"
                }
            }
            ItemDelegate {
                text: qsTr("Config")
                width: parent.width
                onClicked: {
                    stackView.push("ConfigsForm.ui.qml")
                    drawer.close()
                    toolheader.text = "Config"
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

