import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQml.Models 2.11
import "delegates"
import "stylings"
import "items"
Page {
    id: configpage
    title: qsTr("Config")
    width: 400
    height: 750
    property var appconfigs
    property var baker
    header: PageHeader {
        Row {
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter 
            Text {
                text: qsTr("Application Path")
                font.pixelSize: 24
                color: "white"
            }
        }
    }

    // Body
    PageBody {
        ListView {
            x: 5; y: 10
            width: 600; height: 600
            spacing: 5
            delegate: AppConfigDelegate {
                textColor:"black"
                width: 600
            }
            populate: Transition {
                NumberAnimation { property: "opacity"; from: 0; to: 1.0; duration: 500 }
                NumberAnimation { 
                    properties: "y"; duration: 500;
                    easing.type: Easing.InOutQuad; }
            }

            Component.onCompleted: {
                // Delay load model for animation
                model = appconfigs
            }
        }
    }

    footer: PageFooter {
        Row {
            spacing: 10
            anchors.horizontalCenter: parent.horizontalCenter
            anchors.verticalCenter: parent.verticalCenter      
            Button {
                width: 150
                text: "Save Configs"
                onClicked: {
                    console.log(baker.allAppsInfo())
                }
            }
        }
    }
    // Styling
    
}
