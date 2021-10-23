'use strict';

if (process.platform === 'win32'
    || ['ia32', 'x32', 'x64'].includes(process.arch)) {
  return console.log('{}');
}

const BuildEnvironment = require('buildcheck');

const be = new BuildEnvironment();

const gyp = {
  defines: [],
  libraries: [],
  sources: [
    'include/internal/hwcaps.h',
    'include/internal/unix_features_aggregator.h',
    'src/hwcaps.c',
    'src/unix_features_aggregator.c',
  ],
};

be.checkHeader('c', 'dlfcn.h');

if (be.checkDeclared('c', 'getauxval', { headers: ['sys/auxv.h'] }))
  gyp.defines.push('HAVE_STRONG_GETAUXVAL=1');

// Add the things we detected
gyp.defines.push(...be.defines(null, true));
gyp.libraries.push(...be.libs());

console.log(JSON.stringify(gyp, null, 2));
