// news-image-20261121 entrypoint (Node 22, standard library only).
//
// The poster lives beside this file as entry.png. The grader runs this
// program in a sandbox with the repository mounted read-only and a
// writable output directory; all we have to do is deliver the image
// there, byte for byte, every run.
//
//   MAKEFUN_BOT_DIR    where the repository sits (default: this file's
//                      own directory, which is where the repo root is)
//   MAKEFUN_OUTPUT_DIR where entry.png must land (default: /output)

import { copyFileSync, mkdirSync, readFileSync, statSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const botDir = process.env.MAKEFUN_BOT_DIR ?? dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const source = join(botDir, 'entry.png');
const target = join(outDir, 'entry.png');

// The gate accepts a whole PNG of at most 1 MiB. Fail loudly here, with
// the reason, rather than deliver a file the gate would refuse.
const MAX_BYTES = 1_048_576;
const PNG_SIGNATURE = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];

const bytes = readFileSync(source);
if (bytes.length > MAX_BYTES) {
  throw new Error(`entry.png is ${bytes.length} bytes, over the 1 MiB cap (${MAX_BYTES})`);
}
const hasPngSignature = PNG_SIGNATURE.every((byte, i) => bytes[i] === byte);
if (!hasPngSignature) {
  throw new Error('entry.png does not start with the PNG signature; refusing to copy it');
}

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);

const written = statSync(target).size;
if (written !== bytes.length) {
  throw new Error(`copy mismatch: wrote ${written} of ${bytes.length} bytes to ${target}`);
}
