import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQml.Models 2.11
import QtQuick.Layouts 1.11
Page {
    id: configpage
    title: qsTr("Config")
    width: 400
    height: 800
    contentWidth: 400
    contentHeight: 800
    property var appconfigs
    
    // Components Init
    Component {     //instantiated when header is processed
        id: bannercomponent
        Rectangle {
            id: banner
            width: parent.width; height: 50
            gradient: clubcolors
            radius: 2
            Text {
                anchors.centerIn: parent
                text: qsTr("Application Path")
                font.pixelSize: 24
                color: "white"
            }
        }
    }
    
    Component {
        id: appdelegate
        Item {
            width: configpage.width
            height: 100
            ColumnLayout {            
                anchors.fill: parent
                RowLayout {
                    spacing: 5
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
                    spacing: 5
                    Label {
                        Layout.alignment: Qt.AlignRight
                        text: '<b>Path:</b>'
                        font.pointSize: 10
                    }
                    TextField {
                        Layout.fillWidth: true
                        width:300
                        text: model.modelData.apppath
                        font.pointSize: 8

                    }
                }
            }
        }
    }

    // Body

    ListView {
        // anchors.fill: parent.fill
        width: parent.width
        height: parent.height
        header: bannercomponent
        delegate: appdelegate
        model: appconfigs
        Component.onCompleted: {
            console.log(appconfigs)
        }
    }
    // Styling
    Gradient {
        id: clubcolors
        GradientStop { position: 0.0; color: "#B28B4B"}
        GradientStop { position: 0.6; color: "#E8A02B"}
    }

}
