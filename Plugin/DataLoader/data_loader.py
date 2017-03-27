# -*- coding: utf-8 -*-
"""
/***************************************************************************
 DataLoader
                                 A QGIS plugin
 Plugin for Data visualisation
                              -------------------
        begin                : 2017-03-05
        git sha              : $Format:%H$
        copyright            : (C) 2017 by Sagar
        email                : jas_96@hotmail.co.uk
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
from __future__ import print_function
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from data_loader_dialog import DataLoaderDialog
import os.path
from Loader import loader
from pop_up_dialog import PopUpDialog


class DataLoader:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'DataLoader_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)


        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&Data Loader')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'DataLoader')
        self.toolbar.setObjectName(u'DataLoader')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('DataLoader', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        # Create the dialog (after translation) and keep reference
        self.dlg = DataLoaderDialog()

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/DataLoader/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'ECMWF loader'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&Data Loader'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""

	print("Checking dependencies")
	depend = self.checkDependencies()
        print (depend)


        ChoiceList = ["Snow Depth", "Total Cloud Cover", "10m V Wind", "2m Temperature", "Total Column Water Vapour", "Specific Humidity", "Solar Duration", "Snowfall", "Relative Humidity", "Surface Pressure", "10m U Wind"]
        self.dlg.listWidget.clear() #widget needs to be cleared every time we open window, otherwise it would keep adding elements
        self.dlg.listWidget.addItems(ChoiceList)


        print("loading classes")
	#class creating
        load = loader()


        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
	    resultlist = []
            items = self.dlg.listWidget.count()
            for i in range(items):
                if self.dlg.listWidget.isItemSelected(self.dlg.listWidget.item(i)) == True:
##                    selectedItems.append(self.dlg.listWidget.indexFromItem(self.dlg.listWidget.item(i)))
                    print(i)
                    resultlist.append(i)

            ch1 = self.dlg.checkBox.isChecked()
            ch2 = self.dlg.checkBox_2.isChecked()
            ch3 = self.dlg.checkBox_3.isChecked()
            ch4 = self.dlg.checkBox_4.isChecked()

            #calculating time from checkbox and putting it into right format
            time=""
            if(ch1):
                time+="00/"
            if(ch2):
                time+="06/"
            if(ch3):
                time+="12/"
            if(ch4):
                time+="18/"
            time = time[:-1]
	    if time == "" :
		self.popup = PopUpDialog("Choose at least one time of day")
		self.popup.show()
	    elif resultlist == []:
		self.popup = PopUpDialog("Choose at least one type of data")
		self.popup.show()
	    else:
		date1 = self.dlg.dateEdit.date().toPyDate()
                date2 = self.dlg.dateEdit_2.date().toPyDate()
                load.loadData(time, date1.strftime("%Y-%m-%d")+"/to/"+date2.strftime("%Y-%m-%d"), resultlist)
 
                pass

    def checkDependencies(self):
        try:
	    import crayfish
	    import qgis
	    import ecmwfapi
	except ImportError:
	    print ("missing some imports: "+sys.exc_info()[0])
	    return "missing some imports: "+sys.exc_info()[0]
        return "All dependencies are installed"
