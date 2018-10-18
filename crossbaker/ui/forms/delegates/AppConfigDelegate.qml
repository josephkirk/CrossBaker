import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Layouts 1.11
Component {
    Item {
        width: parent.width
        height: 100
        ColumnLayout {            
            anchors.fill: parent
            // padding: 5
            RowLayout {
                Layout.margins: 5
                Label { 
                    Layout.alignment: Qt.AlignRight
                    text: '<b>App Name:</b> '
                    font.pointSize: 10
                }
                Text {
                    text: model.modelData.appname
                    font.pointSize: 12
                    color:"white"
                    }
            }
            RowLayout {
                Layout.margins: 10
                Label {
                    Layout.alignment: Qt.AlignRight
                    text: '<b>Path:</b>'
                    font.pointSize: 10
                }
                TextField {
                    Layout.fillWidth: true
                    text: model.modelData.apppath
                    font.pointSize: 8

                }
            }
        }
    }
}