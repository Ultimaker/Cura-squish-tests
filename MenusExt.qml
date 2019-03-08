import QtQuick 2.1
import com.froglogic.squish.qtquick 0.1

SquishHook {
    priority: 120

    readonly property var objectNameProperties: {
        "StyleItem1": [ "text" ],
    };

    function __isListViewRow( item ) {
        return ( qmlType( item ) == "FocusScope" ) &&
               ( qmlId( item ) == "rowitem" );
    }

    function __isStackViewPage( item ) {
        return ( item.parent && qmlType( item.parent ) == "StackView" );
    }

    function containerFor( item ) {
        for ( var p = item.parent; p; p = p.parent ) {
            if ( isQmlType( p, "ScrollView" ) ) {
                return p;
            }

            if ( __isStackViewPage( p ) ) {
                // Use pages in a StackView as containers for their children
                return p;
            }

            if ( __isListViewRow( p ) ) {
                // Use rows in a ListView as containers for their children
                return p;
            }
        }
        return unhandled;
    }

    function __findParentLoader( item, loaderId )
    {
        for ( var p = item.parent; p; p = p.parent ) {
            if ( qmlType( p ) == "Loader" && qmlId( p ) == loaderId ) {
                return p;
            }
        }
        return null;
    }

    function isIgnored( item ) {

        if ( item.parent ) {
            var itemType = qmlType( item );

            if ( __isStackViewPage( item ) ) {
                // All direct children of StackView are pages on the stack,
                // never ignore them regardless of their type
                return false;
            }

            if ( __isListViewRow( item ) ) {
                /* Rows in a ListView are useful for selecting rows without
                 * clicking on actual cell texts, also they are used as
                 * containers so making them pickable is a good idea.
                 */
                return false;
            }

            if ( __findParentLoader( item, "rowstyle" ) ) {
                return true;
            }

            var loader = __findParentLoader( item, "panelLoader" );
            if ( loader && ( qmlType( loader.parent ) != "RootItem" ) ) {
                /* Ignore panelLoader. They are used to load style specific
                 * resources and as such contain children that may not be
                 * available on all platforms or Qt versions.  One exception is
                 * the panelLoader used to load ApplicationWindow contents
                 * since that would hide most items inside the window.
                 */
                return true;
            }

            var parentType = qmlType( item.parent );
            if ( parentType == "TextField" ) {
                // Ignore direct children in TextField, this skips the
                // actual TextInput as well as placeholderText
                return true;
            }

            if ( isQmlType( item.parent, "AbstractButton" ) ) {
                // Ignore direct children in QtQuickControls2 AbstractButton,
                // essentially skipping styling items for most new controls
                return true;
            }

            if ( isQmlType( item.parent, "ComboBox" ) ) {
                return true;
            }
        }

        return unhandled;
    }

    function isItemReady( item ) {
        for ( var p = item; p; p = p.parent ) {
            if ( isQmlType( p, "StackView" ) && p.busy ) {
                // Items inside a changing StackView are not ready
                return false;
            }
        }
        return unhandled;
    }
}
