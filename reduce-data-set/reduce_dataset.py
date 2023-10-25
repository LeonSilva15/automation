import os
import re
import shutil
import argparse

def reduce_dataset( size, directory, target, types ):
    # Create the target directory if not exists
    if( not os.path.isdir( target ) ):
        os.mkdir( target )
    
    # Copy the files to the reduced dataset directory
    for root_dir, _, files in os.walk( directory ):
        _target = target + root_dir.split( directory )[ 1 ]
        
        if( not os.path.isdir( _target ) ):
            os.mkdir( _target )
            
        filtered_files = list( filter(
            lambda file: re.search(
                '( {} )$'.format( '|'.join( types ) ),
                file,
                flags=re.IGNORECASE ),
                files
            ) )
        
        # Copy at most the desired number of elements
        copy_index = ( len( filtered_files ) // size ) or 1
        count = 0

        for i in range( 0, len( filtered_files ), copy_index ):
            shutil.copyfile( root_dir + '/' + filtered_files[ i ],
                _target + '/' + filtered_files[ i ] )
            
            # Avoid unprecission on dataset size
            count += 1
            if( count >= size ):
                break


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument( '-size', '--size', help='Target dataset size', type=int, default=200 )
    parser.add_argument( '-d', '--directory', help='Source directory', default='./' )
    parser.add_argument( '-t', '--target', help='Target directory' )
    parser.add_argument( '-types', '--types', help='File types', default=[ 'jpeg', 'jpg', 'png' ] )

    args = vars( parser.parse_args() )

    # Get the path to the directory
    abs_path = os.path.abspath( args[ 'directory' ] )

    # Get the specified directory name to work on
    dir_name = abs_path.split( '/' )[ -1 ]
    
    # When no target dirctory was specified, create one by default
    if not args[ 'target' ]:
        parent_path = '/'.join( abs_path.split( '/' )[ :-1 ] )
        target = parent_path + '/reduced_' + dir_name
    else:
        target = os.path.abspath( args[ 'target' ] )

    args[ 'directory' ] = abs_path
    args[ 'target' ] = target

    print( 'Target dataset size: {} '.format( args[ 'size' ] ))
    print( 'Source directory: {} '.format( args[ 'directory' ] ))
    print( 'Target directory: {} '.format( args[ 'target' ] ))
    print( 'File types: {} '.format( args[ 'types' ] ))

    reduce_dataset( **args )
