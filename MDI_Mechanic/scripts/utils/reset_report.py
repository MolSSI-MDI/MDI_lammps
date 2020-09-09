import os
import shutil

def reset_report():
    # Path to this file
    file_path = os.path.dirname(os.path.realpath(__file__))

    # Path to the top-level directory
    base_path = os.path.dirname( os.path.dirname( os.path.dirname( file_path ) ) )

    # Remove the old report
    report_path = os.path.join(base_path, "report")
    if os.path.isdir( report_path ):
        shutil.rmtree( report_path )

    # Copy the base report
    src_location = os.path.join( base_path, "MDI_Mechanic", "base_report")
    dst_location = os.path.join( base_path, "report")
    shutil.copytree( src_location, dst_location )

    # Reset the README.md file
    src_location = os.path.join( base_path, "MDI_Mechanic", "README.base")
    dst_location = os.path.join( base_path, "README.md")
    shutil.copyfile( src_location, dst_location )

if __name__ == "__main__":
    reset_report()
