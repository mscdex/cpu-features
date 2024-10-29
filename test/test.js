'use strict';

const assert = require('assert');

const info = require('../lib/index.js')();

console.log(info);
assert(typeof info === 'object' && info !== null);
assert(typeof info.arch === 'string' && info.arch);
assert(typeof info.flags === 'object' && info.flags !== null);
if (process.platform !== 'darwin' && process.arch !== 'arm64')
  // Assume we are on a known platform
  if (info.arch === 'loong64' || info.arch === 'mips')
    assert(Object.keys(info).length >= 2);
  else
    assert(Object.keys(info).length > 2);
