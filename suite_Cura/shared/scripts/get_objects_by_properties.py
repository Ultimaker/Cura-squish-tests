# -*- coding: utf-8 -*-
# https://kb.froglogic.com/display/KB/Example+-+Finding+child+objects+by+type+and+property+values
class getObjectsByProperties:
#     This class recursively searches for objects
#     It goes through all descendants of the parent object
    
    @classmethod
    def get_objects(cls, parent_obj, property_names_values, max_find_count=-1, verbose=False):
        """Pass negative max_find_count parameter to find all matching objects.
        Special property "type" allows searching for the object type."""

        return cls.get_objects_impl(
            findObject(parent_obj),
            property_names_values,
            max_find_count,
            [],
            verbose)

    @classmethod
    def get_objects_impl(cls, parent_obj, properties_names_values, max_find_count, found_children=[], verbose=False):
        children = object.children(parent_obj)
        
        # Look for matching children
        for c in children:
            if cls.has_properties_and_values(c, properties_names_values, verbose):
                found_children.append(c)
                if len(found_children) == max_find_count:
                    return found_children

        # Look for matching grand-children
        for c in children:
            found_children = cls.get_objects_impl(
                c,
                properties_names_values,
                max_find_count,
                found_children,
                verbose)
            if max_find_count > 0 and len(found_children) >= max_find_count:
                return found_children[:max_find_count]

        return found_children

    @classmethod
    def has_properties_and_values(cls, obj, properties_names_values, verbose):
        # Verify type early to minimize property value comparisons:
        if "type" in properties_names_values:
            # Strip away QML/QtQuick specific appendices to the
            # class name:
            cn = className(obj)
            if "_QMLTYPE_" in cn:
                cn = cn.split("_QMLTYPE_", 1)[0]
            elif "_QML_" in cn:
                cn = cn.split("_QML_", 1)[0]
            if verbose:
                test.log(className(obj))
            if cn != properties_names_values["type"]:
                if verbose:
                    test.log('Type different: Found type "%s" != "%s"' % (cn, properties_names_values["type"]), "Object properties: %s" % cls.obj_to_str(obj))
                return False

        for name, value in properties_names_values.items():
            # Special property "type", already verified above!
            if name == "type":
                continue
            elif not hasattr(obj, name):
                if verbose:
                    test.log('Property not found: "%s"' % name, "Object properties: %s" % cls.obj_to_str(obj))
                return False
            elif obj[name] != value:
                if verbose:
                    test.log('Property different: Property: "%s", actual value: "%s" != "%s"' % (name, obj[name], value), "Object properties: %s" % cls.obj_to_str(obj))
                return False
        if verbose:
            test.log("Object matched: %s" % cls.obj_to_str(obj))
        return True

    @classmethod
    def obj_to_str(cls, obj):
        s = ""
        for name, value in object.properties(obj).items():
            s += '; "%s": "%s"' % (name, value)
        s = s[2:]
        return s