{
  'targets': [
    {
      'target_name': 'cpu_features',
      'type': 'static_library',

      'cflags': [ '-O3' ],

      'include_dirs': [
        'include',
        'include/internal',
      ],
      'sources': [
        'include/cpu_features_cache_info.h',
        'include/cpu_features_macros.h',

        # utils
        'include/internal/bit_utils.h',
        'include/internal/filesystem.h',
        'include/internal/stack_line_reader.h',
        'include/internal/string_view.h',
        'src/filesystem.c',
        'src/stack_line_reader.c',
        'src/string_view.c',
      ],
      'conditions': [
        ['target_arch in "mips mipsel mips64 mips64el"', {
          'sources': [
            'include/cpuinfo_mips.h',
            'src/cpuinfo_mips.c',
          ],
        }],
        ['target_arch=="arm"', {
          'sources': [
            'include/cpuinfo_arm.h',
            'src/cpuinfo_arm.c',
          ],
        }],
        ['target_arch=="arm64"', {
          'sources': [
            'include/cpuinfo_aarch64.h',
            'src/cpuinfo_aarch64.c',
          ],
        }],
        ['target_arch in "ia32 x32 x64"', {
          'sources': [
            'include/internal/cpuid_x86.h',
            'include/cpuinfo_x86.h',
            'src/cpuinfo_x86.c',
          ],
        }],
        ['target_arch in "ppc ppc64"', {
          'sources': [
            'include/cpuinfo_ppc.h',
            'src/cpuinfo_ppc.c',
          ],
        }],

        ['OS=="mac" and target_arch in "ia32 x32 x64"', {
          'defines': [
            'HAVE_SYSCTLBYNAME=1',
          ],
        }],
      ],
      'defines': [
        'NDEBUG',
        'STACK_LINE_READER_BUFFER_SIZE=1024',
      ],

      # Use generated config
      'includes': [
        '../../buildcheck.gypi',
      ],

      'direct_dependent_settings': {
        'include_dirs': [
          'include',
        ],
        'defines': [
          # Manually-tracked git revision
          'CPU_FEATURES_VERSION_REV=545b2e84ec68f4364be1e89309a1404575689226',
        ],
      },
    },
  ],
}
