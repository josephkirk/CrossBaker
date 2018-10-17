import QtQuick 2.11
import QtQuick.Controls 1.4
import QtQuick.Controls 2.4
import QtQml.Models 2.11
Page {
    id: homepage
    title: qsTr("Set up")
    width: 400
    height: 800
    contentWidth: width
    contentHeight: height
    property var model
    property var baker
    property var bakers
    Column {
        // leftPadding: 5
        Rectangle {
            id: bakercombo
            width: parent.width
            height: 50
            color: "gray"
            Row {
                leftPadding: 15
                spacing: 10
                Label {
                    anchors.verticalCenter: parent.verticalCenter
                    text: "Baker"
                    width: 100
                    color: "white"
                    font.bold: true
                    font.family: "san-serif"
                    font.pointSize: 16
                }
                ComboBox {
                    anchors.verticalCenter: parent.verticalCenter
                    width: 200
                    model: bakers
                }
            }
        }
        TreeView {
            id: layerview
            width: homepage.width
            height: 400
            TableViewColumn {
                title: "Title"
                role: "title"
            }

            TableViewColumn {
                title: "Description"
                role: "description"
            }
            Component.onCompleted: {
                if (model!= undefined) {
                    model: model
                }
            }
        }
        Button {
            anchors.right: parent.right
            width: 100
            text: "Run Baker"
            onClicked: baker.run()
        }
    }
}
