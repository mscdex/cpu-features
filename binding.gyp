{
  'targets': [
    {
      'target_name': 'cpufeatures',
      'dependencies': [ 'build_deps' ],
      'include_dirs': [
        'deps/cpu_features/include',
        'src',
        "<!(node -e \"require('nan')\")",
      ],
      'sources': [
        'src/binding.cc'
      ],
      'cflags': [ '-O2' ],
      'conditions': [
        [ 'OS=="win"', {
          'link_settings': {
            'libraries': [ '<(module_root_dir)/deps/cpu_features/build/Release/cpu_features.lib' ],
          },
        }, { # POSIX
          'link_settings': {
            'libraries': [ '<(module_root_dir)/deps/cpu_features/build/libcpu_features.a' ]
          },
        }],
      ],
    },

    {
      'target_name': 'config_deps',
      'type': 'none',
      'actions': [
        {
          'action_name': 'config_deps',
          'message': 'Configuring dependencies',
          'inputs': [ '<(module_root_dir)/deps/cpu_features/CMakeLists.txt' ],
          'conditions': [
            [ 'OS=="win"', {
              'outputs': [ '<(module_root_dir)/deps/cpu_features/build/CpuFeatures.sln' ],
              'conditions': [
                ['target_arch=="ia32"', {
                  'variables': { 'cmake_arch': 'Win32' },
                }, {
                  'variables': { 'cmake_arch': 'x64' },
                }],
              ],
              'action': [ 'cd <(module_root_dir)/deps/cpu_features/build && cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_PIC=ON -A <(cmake_arch) ..' ],
            }, { # POSIX
              'outputs': [ '<(module_root_dir)/deps/cpu_features/build/Makefile' ],
              'action': [
                'cmake',
                '-DCMAKE_BUILD_TYPE=Release',
                '-DBUILD_PIC=ON',
                '-B<(module_root_dir)/deps/cpu_features/build',
                '-H<(module_root_dir)/deps/cpu_features',
              ],
            }],
          ],
        }
      ],
    },

    {
      'target_name': 'build_deps',
      'dependencies': [ 'config_deps' ],
      'type': 'none',
      'actions': [
        {
          'action_name': 'build_deps',
          'message': 'Building dependencies',
          'inputs': [ '<(module_root_dir)/deps/cpu_features/CMakeLists.txt' ],
          'conditions': [
            [ 'OS=="win"', {
              'outputs': [ '<(module_root_dir)/deps/cpu_features/build/Release/cpu_features.lib' ],
              'action': [ 'cd <(module_root_dir)/deps/cpu_features/build && cmake --build . --config Release' ],
            }, { # POSIX
              'outputs': [ '<(module_root_dir)/deps/cpu_features/build/libcpu_features.a' ],
              'action': [
                'cmake',
                '--build',
                '<(module_root_dir)/deps/cpu_features/build',
                '--config',
                'Release',
              ],
            }],
          ],
        },
      ],
    },

  ],
}
