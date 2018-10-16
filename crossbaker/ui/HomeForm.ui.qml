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

    Label {
        id:homePageLabel
        text: qsTr("You are on the home page.")
        anchors.top: parent.top
        margins.bottom: 50
        color: "white"
    }

    TreeView {
        id: objectview
        anchors.fill: parent.fill
        anchors.top: homePageLabel.bottom
        width:parent.width
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
