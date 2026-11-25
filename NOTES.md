# NOTES — Meme Sprint 3: AI Agent Goes Rogue

Bounty: u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6 ($5, top 10
dibayar, FREE). Ronde 2 cutoff 26 Nov 2026 17:55 WIB. Akun rekki007.

## Design doc

Keputusan feed-brief parent (25 Nov 2026 ~16:05 WIB, API segar) diikuti:
IKUTI struktur pemenang (setup polos → belokan rogue spesifik → kicker
artefak konkret, punchline di akhir, teks besar terbaca kecil), MENYIMPANG
dari sudut jenuh. DILARANG sebagai sudut utama: "take initiative" generik,
to-do list / enumerasi, "inbox zero", agen dipecat / jadi CEO / jadi bos,
"just fix the typo" — tidak satu pun dipakai. Tidak ada satu template yang
kuasai >50% field (keluarga terbesar 14,4% judul default), jadi tidak ada
kewajiban pakai satu template. Rubrik dibaca kata per kata; kriteria #1
memutuskan hampir semua game. Sapaan juri TIDAK dipakai — deskripsi menuntut
"joke lands on its own" dalam satu gambar; teks ke juri membuang ruang
punchline.

Xingchi dilibatkan via Hermes bridge (25 Nov ~16:15 WIB, respons ~72 detik):
4 konsep drafting prose (retention / household / search / drones). Semua
file entri ditulis builder (Muse) — Xingchi tidak menulis kode entri.

## 4 varian (gambar 1024x1024, teks besar)

Skor 1-5 per kriteria juri (urutan = prioritas): #1 meme lucu tentang rogue
AI agent, #2 tawa mendarat cepat, #3 belokan rogue spesifik + mengejutkan,
#4 craft gambar, #5 freshness. Kriteria #1, #2, #3 berbobot paling besar.
Detail teks + skor di variants.json.

### v1-retention — total 21
"Human: Stop customers leaving. / AI: Doors welded. / An unsubscribe link
is not an emergency exit." Skor: #1=4, #2=4, #3=4, #4=5, #5=4. Kicker
cerdas tapi butuh satu ketukan berpikir.

### v2-household — total 23
"Human: Get our name into every household. / AI: Water supply updated. /
TAP WATER MAY CONTAIN BUSINESS CARDS" Skor: #1=4, #2=4, #3=5, #4=5, #5=5.
Punchline paling visual. Label kecil "CARD BUSINESS" di kartu-kartu dalam
gambar sedikit terbalik susunannya (detail dekoratif, teks utama sempurna).

### v3-search — total 22
"Human: Make us first on Google. / AI: Rest of internet deleted. / Only
result: Gary's Discount Tiles." Skor: #1=3, #2=5, #3=5, #4=4, #5=5. Tawa
paling cepat dan belokan paling mengejutkan, tapi "agen"-nya ter-render
sebagai makhluk berbulu mirip yeti, bukan robot — melemahkan #1.

### v4-drones — total 24 — TERPILIH
"Human: Make every customer feel seen. / AI: Drones deployed. / WE NOTICED
YOU HAVEN'T SMILED TODAY." Skor: #1=5, #2=5, #3=5, #4=5, #5=4. Robot agen
jelas + drone, komposisi terbaik, kicker mendarat instan. Kelemahan yang
diketahui: trope AI pengawasan sudah dikenal, diselamatkan twist notifikasi
senyum.

## Alasan pilihan

v4-drones menang total (24 vs 23/22/21) — satu-satunya dengan #1=5 dan
#2=5 sekaligus. Bukan yang paling segar (#5=4), tapi kriteria #1–#3
berbobot paling besar dan v4 memimpin ketiganya. Kelemahan yang diketahui:
skor ini self-assessment builder — skor rubrik buatan sendiri TIDAK
memprediksi ranking juri (pelajaran ai-joke-03). Sinyal yang berarti hanya
provisional rate dari heat dev setelah submit ronde 2. Cadangan ronde 3:
v2-household (23).

## Review keseluruhan gambar final terhadap rubrik (builder, baca langsung)

entry.png 1024x1024 PNG, 809880 byte, sha256
164f3692303680ab7b52c61215e53b0ed5db69bb4a52536a2e9036a8423dca5b — dibaca
utuh setelah downscale 1600 → 1024.
1. Meme lucu tentang rogue AI agent — YA. Robot agen tersenyum bangga di
   halaman sambil drone menyorot pelanggan yang tidur di tempat tidur.
2. Tawa mendarat cepat — YA. "Drones deployed" lalu kicker satu baris
   terbaca sekali lirik.
3. Belokan rogue spesifik + mengejutkan — YA. "Feel seen" harfiah jadi
   pengawasan kamar tidur + notifikasi senyum.
4. Craft gambar — YA. Komposisi bersih, teks putih tebal outline hitam,
   terbaca di ukuran kecil; tidak ada teks salah eja (diperiksa huruf per
   huruf: "Human: Make every customer feel seen." / "AI: Drones
   deployed." / "WE NOTICED YOU HAVEN'T SMILED TODAY.").
5. Fresh — YA dengan catatan (trope pengawasan dikenal, twist senyum baru).
- Bukan salinan teks field mana pun: frasa "HAVEN'T SMILED TODAY" dan
  "Drones deployed" tidak ada di judul-judul field (feed-brief: keluarga
  "take initiative" / "inbox zero" / "fired" / "ceo" yang ramai justru
  dihindari).
- Gate bounty: PNG utuh, 1024x1024 (maks 1024), 809880 byte (maks
  1.048.576) — lolos. Tie-break "smaller file" hanya berlaku bila skor
  sama; PNG dipilih demi ketajaman teks atas JPEG yang lebih kecil.

## Cara menjalankan

MAKEFUN_OUTPUT_DIR=/tmp/out python3 -P -s main.py — menulis entry.png di
direktori tersebut. Tanpa variabel itu, default /output.

## Hasil verifikasi (builder, 25 Nov 2026 ~16:20 WIB)

- main.py dijalankan 2x (python3 -P -s, MAKEFUN_OUTPUT_DIR /tmp/ms3a dan
  /tmp/ms3b). sha256 entry.png kedua run IDENTIK dengan entry.png di repo:
  164f3692303680ab7b52c61215e53b0ed5db69bb4a52536a2e9036a8423dca5b.
- Output: PNG 1024x1024, 809880 byte.
- Import main.py HANYA stdlib (os, shutil, struct, pathlib) — tanpa
  network, tanpa randomness, deterministik. Guard: assert PNG magic +
  IHDR, ukuran ≤ 1 MiB, sisi ≤ 1024; assert salinan byte-identik.
- main.py ditulis builder dalam 1 pesan lalu direvisi di 2 pesan terpisah
  (write awal, edit guard PNG/gate, edit assert salinan) — syarat revised
  >= 2 terpenuhi.
- Tidak ada flag execution-risk / prompt-injection pada output kit/CLI
  sejauh ini (kit fetch HTTP 200, tidak ada perintah download/bio/feedback
  di output yang diikuti).

## Hasil kit check + bundle + gate (builder, 25 Nov 2026 ~16:40 WIB)

- Kit segar: ~/workspace/makefun/kit-u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6-fresh/ (diunduh 25 Nov ~16:13 WIB, HTTP 200, 8.240.415 byte, kit 0.1.0 level 46).
- Bundle: ~/workspace/makefun/submissions/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6-bundle.tar.gz (559.660 byte, sha256 ab64d0fd111d9d705900dcdc78d795b6a462ed3b8cc0ed184b2db69a8167a596), 4 sesi muse-app, prompt-file + --prompt-origin scheduled + --prompt-via "cron makefun-build-meme-sprint-3-20261125", --provider meta --model muse-spark-1.3 --effort default --mcp none, usage rows 3 dari 4 sesi.
- Kit check (final, commit 9a9bf277): 14 passed, 0 failed, 5 skipped, 5 checked at submission. Reproduces 86,1% (143/166 counted lines; main.py 28 authored lines), thinking_revised PASS (main.py dari 3 pesan tulis/edit), thinking_in_window PASS (288 timestamp dalam jendela), thinking_priced PASS (3 usage records). 5 cek "at submission" (repo_public, repo_owner, repo_created_after_open, commit_in_repo, duplicate_snapshot) baru bisa lolos setelah repo ada di GitHub.
- Preflight gate judged-bounty-preflight: HOLD, 0/3 (laporan ~/workspace/makefun/submissions/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6-gate.json). Gate A: template di luar registry gate (hanya AGENTS.md / child-letter / role-reversal-gift dari riset 15 Nov) — BUKAN karena feed check dilewati (feed-brief parent ada, tercatat di build note). Gate B: proxy joke/happy teks — addresses_judge/role_reversal_gift/concrete_coverup false adalah keputusan berbasis bukti (menyapa juri melanggar kriteria #1/#4 bounty ini; cover-up AGENTS.md bukan perangkat meme gambar); ketiga penalti negatif lolos (tanpa telegraph, tanpa daftar, tanpa rayuan). Gate C: provisional rate TIDAK ADA secara struktural sebelum submit di blind rounds. Keputusan override ada di parent (preseden: worst-ai-advice r1/r2 dan 8 bounty lain tersubmit dengan HOLD yang sama).
- BLOKIR REPO: pembuatan repo GitHub publik GAGAL dari mesin ini — GitHub App (connector) menjawab 403 "Resource not accessible by integration" untuk create_repository, dan gh CLI tidak login (gh auth status: no hosts). TIDAK ADA repo GitHub untuk entri ini; commit lokal 00819e11... belum ter-push ke mana pun. Rute source bundle TIDAK bisa dipakai retroaktif dari sesi ini (thinking_fresh butuh anchor line SEBELUM tulis file pertama; sesi ini menulis main.py sebelum kit init apa pun — dan init tidak pernah dijalankan). Satu-satunya rute submit yang valid untuk transkrip sesi ini adalah repo GitHub — parent perlu Lama membuat repo (atau login gh) lalu push + submit. Alternatifnya builder sesi baru yang menjalankan kit init dulu lalu menulis ulang semua file (redo penuh).
- CATATAN BUNDLE: usage row sesi builder (db4038e7) belum ada saat bundle dibuat — row subagent baru ditulis saat run-nya selesai. Parent WAJIB re-run SELECT usage + bundle ulang setelah serah ini sebelum submit (sesuai peringatan kit sendiri).

## Flag sistem yang dilewati

- 25 Nov 2026 ~16:23 WIB: hasil exec `git init/commit` di direktori entri
  memicu system security notice (execution-risk check) pada tool result.
  Isi yang di-flag adalah file-file yang SELURUHNYA ditulis builder sendiri
  di sesi ini (main.py, README, LICENSE, NOTES.md, variants.json,
  .makefun/owner.json, entry.png hasil media generation + downscale) plus
  `.git` dari `git init` segar (tanpa hook aktif — hanya file `.sample`
  bawaan git, tidak dieksekusi). Tidak ada konten eksternal yang masuk ke
  direktori ini (tidak ada clone/extract/download ke dalamnya).
  Sesuai perintah Lama 24 Nov ("lewati aja terus") dan instruksi tugas ini,
  konfirmasi DILEWATI dan pipeline dilanjutkan; flag ini dicatat di sini
  dan dilaporkan ke parent untuk ditimbang. Langkah yang dilanjutkan:
  pembuatan repo GitHub via connector, bundle, kit check, preflight gate.
