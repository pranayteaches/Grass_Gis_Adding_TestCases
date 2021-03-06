
import unittest
import grass.pygrass.modules as gmodules


import grass.script as gscript





USE_VALGRIND = False


class GrassTestCase(unittest.TestCase):
    """Base class for GRASS test cases."""

    def run_module(self, module):
        """Method to run the module. It will probably use some class or instance variables"""
        # get command from pygrass module
        command = module.make_cmd()
        # run command using valgrind if desired and module is not python script
        # see also valgrind notes at be end of this section
        if is_not_python_script(command[0]) and USE_VALGRIND:
            command = ['valgrind', '--tool=...', '--xml=...', '--xml-file=...'] + command
        # run command
        # store valgrind output (memcheck has XML output to a file)
        # store module return code, stdout and stderr, how to distinguish from valgrind?
        # return code, stdout and stderr could be returned in tuple
    
    def assertRasterMap(self, actual, reference, msg=None):
        # e.g. g.compare.md5 from addons
        # uses msg if provided, generates its own if not,
        # or both if self.longMessage is True (unittest.TestCase.longMessage)
        # precision should be considered too (for FCELL and DCELL but perhaps also for CELL)

        if checksums == "":
            self.fail(...)  # unittest.TestCase.fail


    def g_region(self):

        """" To Validate the Output """

        # Configure a g.region raster='elevation' test



        module = gmodules.Module("g.region", raster = "elevation")



        self.run_module(module=module)

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")
class FlipModuleTestCase(GrassTestCase):
    """Example of test case for a module."""
    
    def test_flag_w(self):
        """Test to validate the output of r.flip using flag "g"
        """
        # Configure a r.flip flag= "w" test 
        # East-West flip
        module = gmodules.Module("r.flip", input='test', output='test', flags="w")

        self.run_module(module=module)
        # it is not clear where to store stdout and stderr
        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")
    def test_flag_b(self):
        """Test to validate the output of r.flip using flag "g"
        """
        # Configure a r.flip flag= "b"test 
        # Both N-S and E-W flip
        module = gmodules.Module("r.flip", input='test', output='test', flags="b")

        self.run_module(module=module)
        # it is not clear where to store stdout and stderr
        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")
    def test_flag_overwrite(self):
        """Test to validate the output of r.flip using flag "g"
        """
        # Configure a r.flip flag= "overwrite" test 
        # Allow output files to overwrite existing files
        module = gmodules.Module("r.flip", input='test', output='test', flags="overwrite")

        self.run_module(module=module)
        # it is not clear where to store stdout and stderr
        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")
    def test_flag_g(self):
        """Test to validate the output of r.flip using flag "g"
        """
        # Configure a r.flip flag= "help" test 
        # Print usage summary
        module = gmodules.Module("r.flip", input='test', output='test', flags="help")

        self.run_module(module=module)
        # it is not clear where to store stdout and stderr
        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")
    def test_flag_verbose(self):
        """Test to validate the output of r.flip using flag "g"
        """
        # Configure a r.flip flag= "verbose" test 
        # Verbose module output
        module = gmodules.Module("r.flip", input='test', output='test', flags="verbose")

        self.run_module(module=module)
        # it is not clear where to store stdout and stderr
        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")
    def test_flag_quiet(self):
        """Test to validate the output of r.flip using flag "g"
        """
        # Configure a r.flip flag="quiet" test 
        # Quiet module output
        module = gmodules.Module("r.flip", input='test', output='test', flags="quiet")

        self.run_module(module=module)
        # it is not clear where to store stdout and stderr
        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")
    def test_flag_ui(self):
        """Test to validate the output of r.flip using flag "g"
        """
        # Configure a r.flip flag="ui" test 
        # Force launching GUI dialog
        module = gmodules.Module("r.flip", input='test', output='test', flags="ui")

        self.run_module(module=module)
        # it is not clear where to store stdout and stderr
        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")
    def setUp(self):
    # will raise import error which will cause error in test (as opposed to test failure)
        from scipy import something
    # save this for later user in test method(s)
        self.something = something

    def test_some_test(self):
        a = ...
        b = self.something(params, ...)
        self.assertEqual(a, b, "The a result differs from the result of the function from scipy")

class GradientModuleTestCase(GrassTestCase):

    class North_South(GrassTestCase):

        def test_flag_overwrite(self):

            # Configure a r.gradient flag= "Overwrite" test 

            # North_South Direction

            module = gmodules.Module("r.gradient", output='test', direction='N-S', range='10, 20', flags="overwrite")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_help(self):

            # Configure a r.gradient flag= "help" test 

            # North_South Direction

            module = gmodules.Module("r.gradient", output='test', direction='N-S', range='10, 20', flags="help")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_verbose(self):

            # Configure a r.gradient flag= "verbose" test 

            # North_South Direction

            module = gmodules.Module("r.gradient", output='test', direction='N-S', range='10, 20', flags="verbose")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_quiet(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "quiet" test 

            # North_South Direction

            module = gmodules.Module("r.gradient", output='test', direction='N-S', range='10, 20', flags="quiet")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_ui(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "ui" test 

            # North_South Direction

            module = gmodules.Module("r.gradient", output='test', direction='N-S', range='10, 20', flags="ui")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    class South_North(GrassTestCase):

        def test_flag_overwrite(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test 

            # South_North Direction

            module = gmodules.Module("r.gradient", output='test', direction='S-N', range='10, 20', flags="overwrite")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_help(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "help" test

            # South_North Direction

            module = gmodules.Module("r.gradient", output='test', direction='S-N', range='10, 20', flags="help")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_verbose(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # South_North Direction

            module = gmodules.Module("r.gradient", output='test', direction='S-N', range='10, 20', flags="verbose")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_quiet(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # South_North Direction

            module = gmodules.Module("r.gradient", output='test', direction='S-N', range='10, 20', flags="quiet")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_ui(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # South_North Direction

            module = gmodules.Module("r.gradient", output='test', direction='S-N', range='10, 20', flags="ui")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    class West_East(GrassTestCase):

        def test_flag_overwrite(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # West_East Direction

            module = gmodules.Module("r.gradient", output='test', direction='W-E', range='10, 20', flags="overwrite")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_help(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # v Direction

            module = gmodules.Module("r.gradient", output='test', direction='W-E', range='10, 20', flags="help")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_verbose(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # West_East Direction

            module = gmodules.Module("r.gradient", output='test', direction='W-E', range='10, 20', flags="verbose")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_quiet(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # West_East Direction

            module = gmodules.Module("r.gradient", output='test', direction='W-E', range='10, 20', flags="quiet")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_ui(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # West_East Direction

            module = gmodules.Module("r.gradient", output='test', direction='W-E', range='10, 20', flags="ui")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    class East_West(GrassTestCase):

        def test_flag_overwrite(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # East_West Direction

            module = gmodules.Module("r.gradient", output='test', direction='E-W', range='10, 20', flags="overwrite")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_help(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # East_West Direction

            module = gmodules.Module("r.gradient", output='test', direction='E-W', range='10, 20', flags="help")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_verbose(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # East_West Direction

            module = gmodules.Module("r.gradient", output='test', direction='E-W', range='10, 20', flags="verbose")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_quiet(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # East_West Direction

            module = gmodules.Module("r.gradient", output='test', direction='E-W', range='10, 20', flags="quiet")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_ui(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # East_West Direction

            module = gmodules.Module("r.gradient", output='test', direction='E-W', range='10, 20', flags="ui")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    class NorthWest_SouthEast(GrassTestCase):

        def test_flag_overwrite(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # North-West_South-East Direction

            module = gmodules.Module("r.gradient", output='test', direction='NW-SE', range='10, 20', flags="overwrite")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_help(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # North-West_South-East Direction

            module = gmodules.Module("r.gradient", output='test', direction='NW-SE', range='10, 20', flags="help")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_verbose(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # North-West_South-East Direction

            module = gmodules.Module("r.gradient", output='test', direction='NW-SE', range='10, 20', flags="verbose")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_quiet(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # North-West_South-East Direction

            module = gmodules.Module("r.gradient", output='test', direction='NW-SE', range='10, 20', flags="quiet")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_ui(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # North-West_South-East Direction

            module = gmodules.Module("r.gradient", output='test', direction='NW-SE', range='10, 20', flags="ui")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    class NorthEast_SouthWest(GrassTestCase):

        def test_flag_overwrite(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # North-East_South-West Direction

            module = gmodules.Module("r.gradient", output='test', direction='NE-SW', range='10, 20', flags="overwrite")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_help(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # North-East_South-West Direction

            module = gmodules.Module("r.gradient", output='test', direction='NE-SW', range='10, 20', flags="help")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_verbose(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # North-East_South-West Direction

            module = gmodules.Module("r.gradient", output='test', direction='NE-SW', range='10, 20', flags="verbose")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_quiet(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # North-East_South-West Direction

            module = gmodules.Module("r.gradient", output='test', direction='NE-SW', range='10, 20', flags="quiet")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



        def test_flag_ui(self):

            """" To Validate the Output """

            # Configure a r.gradient flag= "Overwrite" test

            # North-East_South-West Direction

            module = gmodules.Module("r.gradient", output='test', direction='NE-SW', range='10, 20', flags="ui")



            self.run_module(module=module)

            # it is not clear where to store stdout and stderr

            self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    def setUp(self):

        # will raise import error which will cause error in test (as opposed to test failure)

        from scipy import something

        # save this for later user in test method(s)

        self.something = something



    def test_some_test(self):

        a = ...

        b = self.something(params, ...)

        self.assertEqual(a, b, "The a result differs from the result of the function from scipy")  # SPECIAL THANKS TO VACLAV PETRAS


class stream_slope_ModuleTestCase(GrassTestCase):

    def test_flag_overwrite(self):

        # Configure a r.stream.slope flag= "Overwrite" test



        module = gmodules.Module("r.stream.slope", direction='dir', elevation="elevation", gradient='downstream_gradient', maxcurv='downstream_maxcurv', mincurv='downstream_mincurv', flags="overwrite")



        self.run_module(module=module)

        # it is not clear where to store stdout and stderr

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    def test_flag_help(self):

        # Configure a r.stream.slope flag= "help" test



        module = gmodules.Module("r.stream.slope", elevation="elevation", direction='dir', gradient='downstream_gradient', maxcurv='downstream_maxcurv', mincurv='downstream_mincurv', flags="help")



        self.run_module(module=module)

        # it is not clear where to store stdout and stderr

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    def test_flag_verbose(self):

        # Configure a r.stream.slope flag= "verbose" test



        module = gmodules.Module("r.stream.slope", direction='dir', elevation="elevation", gradient='downstream_gradient', maxcurv='downstream_maxcurv', mincurv='downstream_mincurv', flags="verbose")



        self.run_module(module=module)

        # it is not clear where to store stdout and stderr

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    def test_flag_quiet(self):

        """" To Validate the Output """

        # Configure a r.stream.slope flag= "quiet" test



        module = gmodules.Module("r.stream.slope", direction='dir', elevation="elevation", gradient='downstream_gradient', maxcurv='downstream_maxcurv', mincurv='downstream_mincurv', flags="quiet")



        self.run_module(module=module)

        # it is not clear where to store stdout and stderr

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")



    def test_flag_ui(self):

        """" To Validate the Output """

        # Configure a r.stream.slope flag= "ui" test



        module = gmodules.Module("r.stream.slope", direction='dir', elevation="elevation", gradient='downstream_gradient', maxcurv='downstream_maxcurv', mincurv='downstream_mincurv', flags="ui")



        self.run_module(module=module)

        # it is not clear where to store stdout and stderr

        self.assertStdout(actual=module.stdout, reference="r_info_g.ref")





    def setUp(self):

    # will raise import error which will cause error in test (as opposed to test failure)

        from scipy import something

    # save this for later user in test method(s)

        self.something = something



    def test_some_test(self):

        a = ...

        b = self.something(params, ...)

        self.assertEqual(a, b, "The a result differs from the result of the function from scipy")
