import QtQuick 2.11
import QtQuick.Controls 2.4
import QtQuick.Controls 1.4
import Qt.labs.folderlistmodel 2.11
import QtQml.Models 2.11
Page {
    id: homePage
    title: qsTr("Home")
    width: 400
    height: 800


    ScrollView {
        anchors.fill: parent
        Column {
            spacing: 2
            Label {
                text: qsTr("You are on the home page.")
            }

            TreeView {
                id: objectview
                FolderListModel {
                    id: folderModel
                    nameFilters: ["*.obj", "*.fbx"]
                    rootFolder: "D:/test/marmosetBaker"
                    showDirs: true
                    showDotAndDotDot: true
                }
                model: folderModel
                selection: ItemSelectionModel {
                    model: folderModel
                }
                TableViewColumn {
                    title: "Name"
                    role: "fileName"
                }

            }
        }
    }
}
