import QtQuick 2.11
import QtQuick.Controls 2.4

Page {
    width: 400
    height: 800
    title: qsTr("Page 1")

    Label {
        text: qsTr("You are on Page 1.")
        anchors.centerIn: parent
    }

    TextEdit {
        id: textEdit
        x: 125
        y: 90
        width: 80
        height: 20
        text: qsTr("Text Edit")
        font.bold: true
        font.family: "Courier"
        horizontalAlignment: Text.AlignLeft
        font.pixelSize: 12
    }

    CheckBox {
        id: checkBox
        x: 9
        y: 398
        width: 196
        height: 32
        text: qsTr("Check Box")
    }

    ListView {
        id: listView
        x: 14
        y: 112
        width: 191
        height: 242
        delegate: Item {
            x: 5
            width: 80
            height: 40
            Row {
                id: row1
                spacing: 10
                Rectangle {
                    width: 40
                    height: 40
                    color: colorCode
                }

                Text {
                    text: name
                    font.bold: true
                    anchors.verticalCenter: parent.verticalCenter
                }
            }
        }
        model: ListModel {
            ListElement {
                name: "Grey"
                colorCode: "grey"
            }

            ListElement {
                name: "Red"
                colorCode: "red"
            }

            ListElement {
                name: "Blue"
                colorCode: "blue"
            }

            ListElement {
                name: "Green"
                colorCode: "green"
            }
        }
    }
}
