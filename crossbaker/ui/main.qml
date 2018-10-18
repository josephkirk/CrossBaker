import QtQuick 2.11
import QtQuick.Controls 2.4
ApplicationWindow {
    id: window
    // flags: Qt.Window
    // objectname: "mainwindow"
    title: qsTr("Cross Baker")
    visible: true
    // active: true
    // flags: Qt.Window
    width: 400
    height: 800
    maximumWidth: 400
    maximumHeight: 800
    minimumWidth: 200
    minimumHeight: 400

    header: ToolBar {
        contentHeight: toolButton.implicitHeight

        Label {
            id: toolheader
            text: "SETUP"
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
                    toolheader.text = "SETUP"
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
        // interactive: false
        Column {
            anchors.fill: parent

            ItemDelegate {
                text: qsTr("SETTINGS")
                width: parent.width
                onClicked: {
                    stackView.push("forms/SettingForm.qml")
                    drawer.close()
                    toolheader.text = "SETTINGS"
                }
            }
            ItemDelegate {
                text: qsTr("CONFIGS")
                width: parent.width
                onClicked: {
                    stackView.push("forms/ConfigsForm.qml", {appconfigs:appconfigsmodel})
                    drawer.close()
                    toolheader.text = "CONFIGS"
                }
            }
        }
    }

    StackView {
        id: stackView
        anchors.fill: parent
        Component.onCompleted: {
            stackView.push(
                "forms/HomeForm.qml", {model:assetModel, baker:baker, bakers:bakers})
        }

    }
}

