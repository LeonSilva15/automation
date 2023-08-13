import sys
import os
import re
import shutil

def reduce_dataset( dataSetSize, directory, target_directory=None, file_types=[] ):
    # Get the path to the directory
    abs_path = os.path.abspath( directory )
    # Get the specified directory name to work on
    dir_name = abs_path.split( '/' )[ -1 ]
    
    # When no target dirctory was specified, create one by default
    if not target_directory:
        parent_path = '/'.join( abs_path.split( '/' )[ :-1 ] )
        target_directory = parent_path + '/reduced_' + dir_name
    
    # Create the target directory if not exists
    if( not os.path.isdir( target_directory ) ):
        os.mkdir( target_directory )
    
    # Copy the files to the reduced dataset directory
    for root_dir, cur_dir, files in os.walk( directory ):
        
        # Create the target directory if not exists
        _target_directory = target_directory + root_dir.split( abs_path )[ 1 ]
        
        if( not os.path.isdir( _target_directory ) ):
            os.mkdir( _target_directory )
            
        filtered_files = list( filter(
            lambda file: re.search(
                '( {} )$'.format( '|'.join( file_types ) ),
                file,
                flags=re.IGNORECASE ),
                files
            ) )
        
        # Copy at most the desired number of elements
        copy_index = ( len( filtered_files ) // dataSetSize ) or 1
        count = 0

        for i in range( 0, len( filtered_files ), copy_index ):
            shutil.copyfile( root_dir + '/' + filtered_files[ i ],
                _target_directory + '/' + filtered_files[ i ] )
            
            # Avoid unprecission on dataset size
            count += 1
            if( count >= dataSetSize ):
                break


if __name__ == '__main__':
    dataSetSize = 200
    directory = './'
    target_directory = None
    file_types = [ 'jpeg', 'jpg', 'png' ]

    if len( sys.argv ) > 1:
        dataSetSize = int( sys.argv[ 1 ] )
    if len( sys.argv ) > 2:
        directory = sys.argv[ 2 ]
    if len( sys.argv ) > 3:
        target_directory = sys.argv[ 3 ]
    if len( sys.argv ) > 4:
        file_types = sys.argv[ 4 ].split(',')

    reduce_dataset( dataSetSize, directory, target_directory, file_types )
