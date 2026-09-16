---
doc_id: NC-OPS-001
doc_title: Panduan Operasional Layanan Internal NusantaraCare
category: kebijakan_dan_sop_layanan_internal
doc_version: "2.0"
effective_date: "2026-07-01"
last_updated: "2026-07-15"
is_active: true
owner: Direktorat Operasi dan Layanan Internal
source_path: data/raw_docs/nusantaracare_panduan_operasional_internal_v2.md
---

# Panduan Operasional Layanan Internal NusantaraCare

## Tujuan, Ruang Lingkup, dan Status Dokumen

Dokumen ini adalah panduan operasional resmi versi 2.0 yang diterbitkan oleh Direktorat Operasi dan Layanan Internal NusantaraCare dan berlaku efektif sejak 1 Juli 2026. Panduan ini menetapkan kebijakan, prosedur standar operasi (SOP), tanggung jawab peran, dan jalur eskalasi yang wajib diikuti oleh seluruh karyawan NusantaraCare dalam mengajukan dan menangani permintaan layanan internal melalui Service Desk. Seluruh ketentuan di dalam dokumen ini bersifat mengikat dan menjadi acuan tunggal bagi Service Desk, Pemilik Layanan, dan seluruh pemohon dalam pengambilan keputusan operasional sehari-hari.

Ruang lingkup panduan ini mencakup empat kategori permintaan utama: pengelolaan akses dan akun aplikasi, penanganan gangguan layanan atau insiden sistem, pengadaan fasilitas dan perlengkapan kerja, serta pelaporan dan eskalasi insiden keamanan. Setiap permintaan wajib dicatat sebagai tiket di Service Portal dan diproses sesuai klasifikasi prioritas dan SLA yang ditetapkan. Dokumen ini juga mengatur tata kelola data dalam tiket, komunikasi antara Service Desk dan pemohon, serta mekanisme penanganan kebijakan yang telah diperbarui atau diarsipkan.

Panduan ini secara eksplisit tidak mencakup lima area berikut: konsultasi medis atau kesehatan karyawan, nasihat hukum atau kepatuhan terhadap peraturan perundang-undangan, penghitungan gaji, tunjangan, atau kompensasi finansial, evaluasi atau konseling kinerja personal, serta permintaan yang berkaitan dengan infrastruktur atau sistem di luar kewenangan Direktorat Operasi dan Layanan Internal. Untuk kebutuhan di luar cakupan tersebut, pemohon diarahkan ke unit kerja atau direktorat yang berwenang sesuai kebijakan NusantaraCare yang terpisah dan tidak diatur dalam panduan ini.

Dokumen ini digunakan sebagai acuan operasional oleh seluruh peran yang terlibat: Pemohon, Atasan Langsung, Service Desk, Pemilik Layanan, Tim Keamanan Informasi, dan Manajer Piket. Service Desk wajib merujuk panduan ini dalam setiap keputusan klasifikasi, penetapan prioritas, dan eskalasi. Panduan ini ditinjau dan diperbarui secara berkala oleh Direktorat Operasi dan Layanan Internal; versi terbaru selalu tersedia di repositori dokumen internal dan menggantikan seluruh versi sebelumnya.
Bagian SOP dalam panduan ini disusun secara mandiri per kategori layanan sehingga pemohon cukup merujuk pada satu bagian yang sesuai dengan jenis permintaannya, tanpa harus membaca keseluruhan dokumen. Setiap bagian SOP dilengkapi dengan contoh konkret yang menggambarkan alur permintaan dari awal hingga selesai, mulai dari pencatatan tiket, persetujuan, hingga penutupan dan dokumentasi penyelesaian.

## Istilah dan Peran

### Definisi Istilah

Dokumen ini menggunakan beberapa pasangan istilah yang memiliki makna setara dan dapat digunakan bergantian di seluruh panduan. Penggunaan istilah yang konsisten membantu pemohon dan Service Desk berkomunikasi tanpa ambiguitas, sekaligus memungkinkan sistem retrieval informasi internal menemukan konteks yang tepat meskipun pemohon menggunakan istilah yang berbeda untuk konsep yang sama.

Pemohon merujuk pada karyawan NusantaraCare yang mengajukan permintaan layanan melalui saluran resmi. Istilah pemohon dan karyawan digunakan secara bergantian di seluruh dokumen ini tanpa perbedaan makna. Setiap permintaan yang diajukan pemohon dicatat sebagai tiket di Service Portal; dengan demikian istilah tiket dan permintaan merujuk pada entitas yang sama dalam sistem pencatatan. Ketika pemohon melaporkan terhentinya atau menurunnya fungsi layanan, laporan tersebut dikategorikan sebagai gangguan. Istilah insiden memiliki arti yang identik dengan gangguan di seluruh panduan ini dan keduanya mengacu pada peristiwa yang menyebabkan layanan tidak berfungsi sebagaimana mestinya. Seluruh tiket, baik yang bersifat permintaan akses, pelaporan peralatan, maupun pelaporan gangguan, wajib disampaikan melalui Service Portal. Istilah portal dan Service Portal digunakan secara bergantian dan selalu merujuk pada aplikasi portal layanan internal NusantaraCare yang dapat diakses melalui kredensial perusahaan.

### Peran dan Tanggung Jawab

Terdapat enam peran dalam alur kerja layanan internal, masing-masing dengan batas wewenang dan titik serah terima yang jelas.

Pemohon adalah karyawan NusantaraCare yang mengajukan permintaan layanan melalui saluran resmi. Pemohon bertanggung jawab menyediakan informasi lengkap dan benar, menyertakan dokumen pendukung, dan menanggapi klarifikasi Service Desk dalam batas waktu yang ditentukan. Pemohon tidak memiliki wewenang mengubah prioritas tiket atau menyetujui permintaannya sendiri.

Atasan Langsung adalah manajer atau supervisor yang membawahi pemohon secara struktural. Atasan Langsung memberikan persetujuan untuk permintaan akses aplikasi dan perlengkapan kerja setelah memverifikasi kesesuaian dengan kebutuhan pekerjaan pemohon. Wewenangnya berhenti pada persetujuan; keputusan teknis dan provisioning dilaksanakan oleh Service Desk dan Pemilik Layanan.

Service Desk adalah tim operasional yang menjadi titik kontak tunggal untuk seluruh permintaan layanan internal. Service Desk mencatat, mengklasifikasikan, menetapkan prioritas berdasarkan dampak dan urgensi, memproses permintaan dalam kewenangannya, dan meneruskan kepada Pemilik Layanan atau Tim Keamanan Informasi bila diperlukan. Service Desk berwenang menolak tiket yang tidak lengkap, tidak melalui saluran resmi, atau di luar cakupan panduan ini.

Pemilik Layanan adalah individu atau tim penanggung jawab sistem, aplikasi, atau infrastruktur tertentu. Pemilik Layanan memberikan persetujuan akses, mengonfirmasi estimasi waktu pemulihan, dan memvalidasi permintaan yang memerlukan keahlian teknis khusus. Tanpa persetujuan Pemilik Layanan, Service Desk tidak dapat memprovisikan akses atau memberikan konfirmasi waktu pemulihan.

Tim Keamanan Informasi menangani seluruh insiden keamanan informasi. Setiap laporan yang mengindikasikan potensi pelanggaran data, akses tidak sah, atau aktivitas mencurigakan wajib dirutekan sebagai P1 tanpa penundaan. Tim ini memiliki wewenang penuh untuk mengisolasi sistem, menangguhkan akses, dan meminta investigasi forensik tanpa persetujuan tambahan.

Manajer Piket adalah personel senior yang bertugas di luar jam kerja normal. Manajer Piket menyetujui pengecualian kebijakan dalam batas yang ditentukan panduan ini, menerima notifikasi seluruh insiden P1, dan mengambil alih koordinasi setelah eskalasi Service Desk. Keputusan Manajer Piket dalam situasi darurat bersifat final.
## Kanal Layanan dan Waktu Operasional

### Saluran Resmi

Service Portal merupakan saluran normal dan utama untuk seluruh permintaan layanan internal NusantaraCare. Setiap pemohon wajib mengakses portal melalui kredensial perusahaan yang sah dan membuat tiket sesuai dengan kategori permintaan yang tersedia. Portal mencatat seluruh riwayat permintaan, status, komunikasi antara pemohon dan Service Desk, serta dokumentasi resolusi dalam satu tempat yang terpusat dan dapat diaudit. Tidak ada permintaan yang dianggap sah secara operasional kecuali tercatat dan memiliki nomor tiket di Service Portal. Pemohon yang belum memiliki akses ke portal karena alasan teknis wajib menghubungi Service Desk melalui telepon untuk mendapatkan bantuan akses awal.

Telepon hanya dapat digunakan sebagai saluran pelaporan untuk gangguan dengan prioritas P1. Pemohon yang melaporkan gangguan P1 melalui telepon tetap wajib membuka tiket di Service Portal setelah panggilan selesai, selama portal dalam kondisi tersedia. Apabila portal tidak tersedia, kewajiban membuka tiket ditangguhkan hingga portal kembali beroperasi, dan panggilan telepon menjadi catatan sementara yang harus dikonversi menjadi tiket oleh Service Desk. Nomor telepon Service Desk tercantum di direktori internal perusahaan dan hanya beroperasi untuk menerima laporan P1.

Alamat email Service Desk, yaitu servicedesk@nusantaracare.internal, hanya dapat digunakan dalam satu kondisi spesifik: ketika Service Portal sedang tidak tersedia atau tidak dapat diakses oleh pemohon karena gangguan teknis pada portal itu sendiri. Dalam kondisi tersebut, subjek email wajib diawali dengan penanda [DARURAT-PORTAL] agar sistem dapat mengidentifikasi dan memprioritaskan email sebagai permintaan darurat. Email yang dikirim tanpa penanda tersebut, atau email yang dikirim saat portal beroperasi normal, tidak akan diproses sebagai permintaan resmi dan akan diabaikan oleh sistem. Pemohon yang menggunakan jalur email darurat tetap diwajibkan membuat tiket di portal segera setelah portal kembali tersedia untuk memastikan permintaan tercatat dalam sistem yang dapat diaudit.

WhatsApp, pesan pribadi melalui aplikasi percakapan apa pun, percakapan lisan di lorong atau ruang rapat, dan saluran tidak resmi lainnya bukan merupakan saluran yang diakui untuk membuat, menindaklanjuti, atau mengeskalasi permintaan layanan. Informasi yang disampaikan melalui saluran tidak resmi tidak mengikat Service Desk, tidak dapat dijadikan dasar untuk klaim pemenuhan SLA atau keluhan keterlambatan, dan tidak tercatat dalam sistem audit. Service Desk berhak mengabaikan permintaan yang disampaikan melalui saluran tidak resmi dan mengarahkan pemohon untuk menggunakan Service Portal.

### Waktu Operasional

Service Desk beroperasi pada hari Senin hingga Jumat, pukul 08.00 hingga 18.00 WIB. Jam operasional ini tidak termasuk hari libur nasional yang ditetapkan oleh pemerintah Republik Indonesia. Pada hari libur nasional, Service Desk hanya menyediakan layanan untuk penanganan insiden P1 dengan mekanisme 24/7. Permintaan P2 dan P3 yang masuk pada hari libur nasional akan diproses pada hari kerja berikutnya, dan perhitungan SLA dimulai pada jam operasional pertama setelah hari libur.

Untuk permintaan P1, Service Desk menyediakan layanan penuh 24 jam sehari dan 7 hari seminggu, termasuk akhir pekan dan seluruh hari libur nasional tanpa pengecualian. Pemohon yang mengalami gangguan P1 di luar jam operasional normal wajib menghubungi Service Desk melalui telepon terlebih dahulu, kemudian melengkapi tiket di portal bila portal tersedia. Apabila portal tidak tersedia di luar jam operasional, pemohon menggunakan jalur email dengan subjek [DARURAT-PORTAL] untuk mencatatkan insiden, dan Service Desk yang bertugas pada shift 24/7 akan mengonversi email tersebut menjadi tiket dalam sistem.

## Klasifikasi Permintaan dan Prioritas

### Prinsip Penetapan Prioritas

Prioritas setiap tiket ditetapkan oleh Service Desk berdasarkan dua faktor objektif: dampak terhadap operasional bisnis dan urgensi penyelesaian. Dampak operasional diukur dari jumlah pengguna yang terdampak atau jumlah fungsi bisnis yang terganggu, bukan dari jabatan atau posisi pemohon dalam struktur organisasi. Urgensi diukur dari seberapa cepat dampak tersebut akan meluas, memburuk, atau menimbulkan kerugian tambahan jika tidak segera ditangani.

Service Desk memiliki wewenang penuh dan eksklusif untuk menetapkan prioritas awal berdasarkan informasi yang tersedia pada saat tiket dicatat. Penetapan prioritas tidak dapat dipengaruhi oleh tekanan, permintaan, atau preferensi pemohon, Atasan Langsung, atau pihak mana pun. Service Desk juga berwenang menaikkan prioritas jika situasi memburuk atau menurunkan prioritas jika workaround yang memadai telah ditemukan dan disetujui. Setiap perubahan prioritas wajib dicatat dalam riwayat tiket disertai alasan perubahan.

### Tingkat Prioritas

Prioritas 1 atau P1 adalah tingkat prioritas tertinggi yang diberikan kepada situasi darurat operasional yang memerlukan respons segera. Sebuah tiket diklasifikasikan sebagai P1 apabila memenuhi salah satu dari dua kriteria berikut: pertama, insiden menyebabkan gangguan atau ketidaktersediaan layanan yang berdampak pada lebih dari 25 orang karyawan secara bersamaan, di mana jumlah 25 orang ini dihitung berdasarkan karyawan yang aktif menggunakan atau memerlukan layanan tersebut pada saat insiden terjadi; kedua, terdapat indikasi, laporan, atau kecurigaan yang beralasan mengenai terjadinya insiden data atau insiden keamanan informasi dalam bentuk apa pun.

Tiket P1 wajib diakui oleh Service Desk dalam waktu 30 menit sejak pencatatan. Pengakuan berarti Service Desk telah meninjau tiket, mengonfirmasi klasifikasi P1, mencatat rencana tindakan awal, dan mengirimkan notifikasi kepada Manajer Piket. Penanganan P1 bersifat 24/7 tanpa terikat jam operasional normal. Manajer Piket wajib menerima notifikasi segera setelah klasifikasi P1 ditetapkan dan mulai memantau perkembangan penanganan.

Prioritas 2 atau P2 diberikan kepada permintaan atau insiden di mana pekerjaan pemohon terhambat secara signifikan dan tidak tersedia solusi sementara atau workaround yang telah disetujui oleh Service Desk atau Pemilik Layanan. P2 tidak berarti pemohon sama sekali tidak dapat bekerja, melainkan bahwa alur kerja normal pemohon tidak dapat dilanjutkan tanpa penyelesaian tiket. Tiket P2 wajib diakui oleh Service Desk dalam waktu 4 jam kerja sejak pencatatan. Perhitungan jam kerja mengikuti jam operasional Service Desk, yaitu Senin hingga Jumat pukul 08.00 hingga 18.00 WIB, dan tidak mencakup akhir pekan atau hari libur nasional.

Prioritas 3 atau P3 adalah tingkat prioritas standar yang diberikan kepada seluruh permintaan yang tidak memenuhi kriteria P1 maupun P2. Kategori ini mencakup pengajuan akses baru untuk karyawan yang jadwal mulainya masih di masa mendatang, permintaan perlengkapan kerja standar dengan tenggat yang masih jauh, pertanyaan prosedural atau informasional, dan permintaan yang telah memiliki workaround yang disetujui sehingga pekerjaan pemohon tetap dapat berjalan. Tiket P3 wajib diakui oleh Service Desk dalam waktu 1 hari kerja sejak pencatatan.

### Contoh Klasifikasi

Contoh pertama: aplikasi penggajian tidak dapat diakses oleh 40 karyawan pada jam kerja. Karena jumlah karyawan terdampak melebihi ambang 25 orang, insiden ini memenuhi kriteria P1. Service Desk wajib mengakui tiket dalam 30 menit dan segera memberi notifikasi kepada Manajer Piket. Penanganan berlangsung 24/7 hingga layanan pulih.

Contoh kedua: seorang karyawan tidak dapat masuk ke modul pelaporan khusus yang hanya digunakannya sendiri. Tidak ada workaround yang memungkinkan karyawan tersebut menghasilkan laporan yang menjadi tanggung jawabnya. Karena pekerjaan terhambat tanpa alternatif, tiket ini diklasifikasikan sebagai P2. Service Desk wajib mengakui tiket dalam 4 jam kerja.

Contoh ketiga: seorang manajer mengajukan permintaan pembuatan akun email untuk karyawan baru yang akan bergabung dalam dua minggu. Tidak ada hambatan operasional saat ini dan tenggat masih jauh. Tiket ini diklasifikasikan sebagai P3 dan diakui dalam 1 hari kerja.

## SOP Permintaan Akses dan Akun

### Input Wajib

Setiap permintaan akses aplikasi atau akun baru wajib disampaikan melalui Service Portal dengan melengkapi seluruh data berikut tanpa kecuali: nomor identitas karyawan pemohon sesuai catatan kepegawaian, nama sistem atau aplikasi yang dimintakan akses sebagaimana tercantum dalam katalog layanan internal, peran atau tingkat akses yang diminta sesuai dengan peran yang tersedia dalam sistem tersebut, alasan bisnis yang menjelaskan secara spesifik mengapa akses tersebut diperlukan untuk pelaksanaan tugas pemohon, dan nama Atasan Langsung pemohon yang akan memberikan persetujuan pertama.

Permintaan yang tidak melengkapi salah satu dari kelima data tersebut akan dikembalikan oleh Service Desk kepada pemohon melalui portal dengan status Menunggu Pemohon dan catatan yang menyebutkan data spesifik yang masih kurang. Pemohon memiliki waktu 3 hari kerja untuk melengkapi data sebelum tiket ditutup otomatis sesuai ketentuan status Menunggu Pemohon. Pemohon tidak dapat memproses permintaannya sendiri atau menyetujui akses untuk dirinya sendiri dalam kondisi apa pun, termasuk dalam situasi darurat.

### Langkah Service Desk

Setelah menerima tiket permintaan akses yang lengkap, Service Desk melakukan tiga langkah verifikasi. Pertama, memverifikasi kelengkapan seluruh data input wajib sebagaimana ditetapkan di atas. Kedua, mengonfirmasi bahwa sistem atau aplikasi yang dimaksud berada dalam cakupan layanan yang dikelola oleh Direktorat Operasi dan Layanan Internal. Ketiga, memeriksa apakah pemohon sudah memiliki akses yang diminta atau akses serupa di sistem yang sama; apabila sudah ada, Service Desk mengonfirmasi kepada pemohon apakah permintaan duplikat ini disengaja atau merupakan kekeliruan.

Apabila sistem tidak termasuk dalam layanan yang dikelola oleh Direktorat Operasi dan Layanan Internal, Service Desk mengembalikan tiket dengan status Selesai dan catatan yang mengarahkan pemohon ke unit kerja atau direktorat yang berwenang. Apabila sistem berada dalam cakupan, Service Desk meneruskan tiket kepada Atasan Langsung pemohon untuk persetujuan pertama. Setelah Atasan Langsung menyetujui, tiket secara otomatis diteruskan kepada Pemilik Layanan dari sistem yang bersangkutan untuk persetujuan kedua. Service Desk tidak dapat memproses provisioning sebelum kedua persetujuan diterima secara lengkap dan tercatat dalam sistem.

Service Desk menargetkan penyelesaian provisioning akses dalam waktu 2 hari kerja setelah kedua persetujuan, yaitu dari Atasan Langsung dan Pemilik Layanan, diterima secara lengkap. Hari kerja dihitung berdasarkan jam operasional Service Desk.

### Akses Sementara dan Pengakhiran Akses

Akses sementara dapat diberikan untuk kebutuhan dengan batas waktu yang jelas dan terdefinisi. Akses sementara memiliki durasi maksimal 14 hari kalender, dihitung sejak tanggal aktivasi, dan wajib mencantumkan tanggal kedaluwarsa yang eksplisit pada saat pengajuan. Pemohon tidak dapat mengajukan akses sementara tanpa menyebutkan tanggal kedaluwarsa, dan Service Desk wajib menolak permintaan akses sementara yang tidak memenuhi ketentuan ini.

Apabila pemohon memerlukan perpanjangan akses sementara, pemohon wajib mengajukan permintaan akses baru melalui Service Portal sebelum tanggal kedaluwarsa akses yang sedang berjalan. Tidak ada mekanisme perpanjangan otomatis; setiap perpanjangan diperlakukan sebagai permintaan baru yang memerlukan persetujuan Atasan Langsung dan Pemilik Layanan seperti permintaan awal. Akses sementara yang telah kedaluwarsa akan dinonaktifkan secara otomatis oleh sistem pada pukul 00.00 WIB di hari setelah tanggal kedaluwarsa, tanpa notifikasi tambahan kepada pemohon.

Hak akses pemohon ke seluruh sistem NusantaraCare berakhir pada hari kerja terakhir pemohon yang bersangkutan. Bagian Sumber Daya Manusia wajib memberitahukan tanggal hari kerja terakhir setiap karyawan yang akan berakhir masa kerjanya kepada Service Desk minimal 3 hari kerja sebelum tanggal tersebut, untuk memungkinkan pencabutan akses yang terencana dan terdokumentasi. Dalam kondisi pemutusan hubungan kerja yang bersifat mendadak atau segera, Atasan Langsung dari karyawan yang bersangkutan wajib segera memberitahukan Service Desk melalui telepon dan tiket P1 untuk penonaktifan akses sesegera mungkin tanpa menunggu notifikasi dari Bagian Sumber Daya Manusia.

### Larangan Kredensial

Kata sandi dalam bentuk apa pun, kode autentikasi multi-faktor atau MFA, kunci API, token akses, sertifikat digital, dan segala bentuk kredensial autentikasi lainnya tidak boleh diminta, dituliskan, ditempelkan, diunggah sebagai lampiran, atau dikirimkan dalam bentuk apa pun melalui sistem tiket. Service Desk tidak akan pernah meminta informasi kredensial dari pemohon melalui tiket, telepon, email, atau saluran komunikasi apa pun. Pemohon yang menerima permintaan kredensial yang mengatasnamakan Service Desk wajib menolak permintaan tersebut dan segera melaporkannya sebagai insiden keamanan.

Pelanggaran terhadap larangan kredensial, baik yang disengaja maupun tidak disengaja, akan dicatat sebagai insiden keamanan dan segera dirutekan kepada Tim Keamanan Informasi dengan prioritas P1. Kredensial yang tidak sengaja tercantum dalam tiket akan dihapus oleh Service Desk atau Tim Keamanan Informasi dan dianggap telah terekspos, sehingga wajib segera dinonaktifkan dan diganti.

### Contoh Lengkap

Seorang pemohon dengan nomor karyawan NC-4021 mengajukan akses ke sistem manajemen inventaris dengan peran "Petugas Gudang" karena tugas barunya mencakup pencatatan stok. Pemohon mengisi formulir di Service Portal dan menyebutkan Atasan Langsungnya, Ibu Ratna.

Service Desk memverifikasi kelengkapan data dan cakupan sistem, lalu meneruskan tiket kepada Ibu Ratna untuk persetujuan pertama. Setelah Ibu Ratna menyetujui, tiket diteruskan kepada Pemilik Layanan sistem inventaris, Bapak Dodi, untuk persetujuan kedua. Setelah kedua persetujuan diterima, Service Desk memprovisikan akses dalam waktu 1 hari kerja. Pemohon menerima notifikasi bahwa akun telah aktif.

## SOP Gangguan Layanan dan Eskalasi

### Pencatatan Insiden

Setiap gangguan atau insiden layanan wajib dicatat sebagai tiket di Service Portal sesegera mungkin setelah kejadian diketahui. Untuk gangguan dengan prioritas P1, pemohon wajib menghubungi Service Desk melalui telepon setelah membuka tiket di portal, selama portal dalam kondisi tersedia. Apabila portal tidak tersedia, pemohon menghubungi Service Desk melalui telepon terlebih dahulu dan Service Desk yang akan mencatatkan tiket setelah portal kembali beroperasi.

Service Desk bertanggung jawab mencatat informasi minimum berikut dalam setiap tiket insiden: waktu kejadian atau waktu pertama kali gejala diamati, sistem atau layanan spesifik yang terdampak, gejala yang diamati secara objektif termasuk pesan kesalahan yang muncul, perkiraan jumlah pengguna yang terdampak berdasarkan laporan pemohon, dan langkah-langkah yang sudah dicoba oleh pemohon sebelum melapor. Informasi yang lengkap pada saat pencatatan awal akan mempercepat proses diagnosis dan eskalasi. Tanpa catatan insiden yang memenuhi persyaratan minimum, proses eskalasi dan investigasi tidak dapat berjalan sesuai SLA yang ditetapkan.

### Alur Penanganan Berdasarkan Prioritas

Untuk insiden P1, Service Desk memberikan pembaruan status kepada pemohon dan seluruh pemangku kepentingan yang terdampak setiap 30 menit sejak insiden dicatat. Pembaruan mencakup status penanganan terkini, langkah investigasi atau pemulihan yang sedang dijalankan, dan perkiraan waktu penyelesaian bila telah tersedia dan telah dikonfirmasi oleh Pemilik Layanan. Service Desk dapat meningkatkan frekuensi pembaruan jika situasi berkembang cepat, tetapi tidak boleh mengurangi frekuensi di bawah 30 menit selama insiden masih berstatus P1.

Apabila setelah 60 menit sejak pencatatan insiden P1 belum ditemukan solusi sementara atau workaround yang memadai, Service Desk wajib melakukan eskalasi penuh kepada Manajer Piket. Eskalasi penuh berarti Manajer Piket mengambil alih koordinasi penanganan, memiliki wewenang untuk mengerahkan sumber daya tambahan dari unit mana pun, dan dapat menyetujui tindakan pemulihan di luar prosedur standar bila situasi memerlukan. Service Desk tetap bertugas memberikan pembaruan berkala dan mendukung pelaksanaan teknis sesuai arahan Manajer Piket.

Untuk insiden P2, Service Desk memberikan pembaruan status satu kali per hari kerja. Pembaruan disampaikan melalui portal dan dapat dilihat oleh pemohon pada halaman tiket yang bersangkutan. Untuk insiden P3, pembaruan hanya diberikan saat status tiket berubah secara signifikan, misalnya dari Sedang Diproses menjadi Menunggu Pemohon atau menjadi Selesai. Pemohon tidak perlu menghubungi Service Desk secara terpisah untuk menanyakan status di luar jadwal pembaruan yang telah ditetapkan, karena seluruh informasi status tersedia secara real-time di portal.

### Batasan Komunikasi Waktu Pemulihan

Service Desk tidak diperkenankan menjanjikan, mengonfirmasi, atau memberikan estimasi waktu pemulihan layanan kepada pemohon sebelum mendapatkan konfirmasi tertulis dari Pemilik Layanan dari sistem yang terdampak. Informasi estimasi yang belum dikonfirmasi oleh Pemilik Layanan tidak boleh disampaikan kepada pemohon dalam bentuk apa pun, termasuk secara lisan melalui telepon. Apabila pemohon menanyakan estimasi waktu pemulihan, Service Desk wajib menjawab bahwa konfirmasi sedang dimintakan kepada Pemilik Layanan dan estimasi akan disampaikan segera setelah tersedia. Pelanggaran terhadap batasan ini dapat menimbulkan ekspektasi yang tidak terpenuhi dan merusak kepercayaan pemohon terhadap Service Desk.

### Kondisi Eskalasi

Eskalasi dari Service Desk kepada Manajer Piket terjadi dalam dua kondisi spesifik. Pertama, insiden P1 yang belum memiliki workaround yang disetujui setelah 60 menit sejak pencatatan tiket. Kedua, situasi apa pun yang menurut penilaian profesional Service Desk memerlukan keputusan atau wewenang yang berada di luar batas kewenangan Service Desk sebagaimana ditetapkan dalam panduan ini.

Eskalasi dari Service Desk kepada Pemilik Layanan terjadi ketika penanganan insiden atau permintaan memerlukan akses administratif, keahlian teknis spesifik, atau keputusan konfigurasi pada sistem yang berada di bawah kewenangan Pemilik Layanan tersebut. Pemilik Layanan wajib merespons eskalasi dalam waktu yang wajar sesuai dengan prioritas tiket.

Eskalasi kepada Tim Keamanan Informasi terjadi segera setelah Service Desk mengidentifikasi atau menerima laporan yang mengandung indikasi insiden keamanan. Eskalasi ini tidak memerlukan verifikasi, persetujuan, atau pertimbangan tambahan. Service Desk wajib meneruskan laporan apa adanya tanpa melakukan penyaringan atau penilaian terhadap validitas laporan.

### Contoh Lengkap

Pada hari Selasa pukul 10.00 WIB, sistem email internal tidak dapat diakses oleh sekitar 60 karyawan. Seorang pemohon membuka tiket di Service Portal lalu menghubungi Service Desk melalui telepon.

Service Desk mencatat insiden sebagai P1 pada pukul 10.05, mengirim notifikasi ke Manajer Piket, dan memberikan pembaruan setiap 30 menit. Setelah 60 menit tanpa workaround, Service Desk melakukan eskalasi penuh kepada Manajer Piket yang mengoordinasikan Pemilik Layanan sistem email. Pemilik Layanan mengonfirmasi estimasi pemulihan 2 jam. Layanan pulih pada pukul 13.15 dan Service Desk menutup tiket dengan ringkasan penyelesaian.

## SOP Fasilitas dan Perlengkapan Kerja

### Permintaan Standar

Permintaan perlengkapan kerja standar, yang mencakup tetapi tidak terbatas pada laptop, komputer desktop, monitor, keyboard, mouse, headset, webcam, dan perangkat pendukung lainnya yang tercantum dalam katalog perlengkapan internal, wajib diajukan melalui Service Portal minimal 5 hari kerja sebelum tanggal kebutuhan. Pemohon wajib menyertakan tiga informasi dalam tiket permintaan: jenis dan spesifikasi perlengkapan yang diminta sesuai dengan katalog yang tersedia, tanggal kebutuhan yang realistis dan sesuai dengan tenggat pengajuan, dan alasan bisnis yang menjelaskan mengapa perlengkapan tersebut diperlukan untuk pelaksanaan tugas.

Atasan Langsung pemohon wajib memberikan persetujuan sebelum tiket diproses lebih lanjut oleh Service Desk. Persetujuan Atasan Langsung menandakan bahwa permintaan sesuai dengan kebutuhan pekerjaan pemohon. Setelah disetujui oleh Atasan Langsung, Service Desk meneruskan permintaan ke unit pengadaan untuk proses pemenuhan. Tiket tetap berada dalam pemantauan Service Desk hingga perlengkapan diterima oleh pemohon dan dikonfirmasi dalam sistem.

Permintaan yang diajukan kurang dari 5 hari kerja sebelum tanggal kebutuhan tidak dapat dijamin pemenuhannya pada tanggal yang diminta. Service Desk akan memproses permintaan tersebut sesuai prioritas P3 dan mengomunikasikan kepada pemohon bahwa tanggal pemenuhan mungkin melampaui tanggal kebutuhan yang diminta, kecuali permintaan tersebut memenuhi syarat pengecualian permintaan di hari yang sama.

### Pengecualian Permintaan Hari yang Sama

Permintaan perlengkapan yang harus dipenuhi pada hari yang sama hanya dapat diproses jika memenuhi salah satu dari tiga kondisi berikut, dan tidak ada kondisi lain yang diakui sebagai pengecualian.

Kondisi pertama: permintaan diajukan untuk mengatasi risiko keselamatan, misalnya perangkat yang mengeluarkan asap, kabel daya yang terbuka, atau kerusakan fisik yang dapat melukai pengguna.

Kondisi kedua: permintaan diperlukan untuk memulihkan layanan dari insiden P1 yang sedang berlangsung, misalnya mengganti laptop yang mengalami kegagalan total dan menjadi penyebab ketidakmampuan pemohon menjalankan fungsi yang terdampak insiden P1.

Kondisi ketiga: permintaan diajukan untuk karyawan yang sedang menjalani hari pertama kerja dan kegagalan penyediaan perlengkapan disebabkan oleh kesalahan administrasi onboarding yang terdokumentasi.

Setiap permintaan di hari yang sama yang memenuhi salah satu dari ketiga syarat di atas wajib mendapatkan persetujuan dari Manajer Piket sebelum diproses. Tanpa persetujuan Manajer Piket, permintaan di hari yang sama tidak dapat dipenuhi. Service Desk bertanggung jawab memverifikasi pemenuhan syarat dan meneruskan permintaan kepada Manajer Piket untuk keputusan akhir.
### Pelaporan Peralatan Hilang atau Rusak

Peralatan yang hilang atau rusak tidak dilaporkan melalui mekanisme permintaan pengadaan standar, melainkan sebagai insiden melalui kategori pelaporan insiden di Service Portal. Pemohon wajib segera membuka tiket dengan kategori insiden dan melaporkan kronologi kehilangan atau kerusakan secara rinci, termasuk waktu terakhir peralatan diketahui dalam kondisi baik, lokasi kejadian, dan saksi bila ada. Service Desk mencatat laporan dan meneruskannya kepada unit yang berwenang untuk pencatatan dan tindak lanjut.

Peralatan yang rusak karena pemakaian normal dalam batas kewajaran tetap dilaporkan melalui mekanisme pelaporan insiden yang sama. Setelah dilaporkan, kerusakan dinilai oleh Service Desk atau unit teknis terkait. Apabila kerusakan tidak menyebabkan gangguan yang memenuhi kriteria P1 atau P2, tiket diproses sesuai prioritas P3. Apabila kerusakan menyebabkan gangguan yang memenuhi kriteria P1 atau P2, tiket diklasifikasikan sesuai prioritas gangguan yang ditimbulkan, bukan sebagai permintaan pengadaan.

### Contoh Lengkap

Seorang karyawan memerlukan laptop pengganti karena perangkatnya mengalami kerusakan layar yang membuat tampilan tidak terbaca. Kerusakan tidak terkait insiden P1, bukan risiko keselamatan, dan bukan hari pertama kerja. Karyawan tersebut mengajukan tiket di Service Portal pada tanggal 5 Juli dengan tanggal kebutuhan 14 Juli, yaitu 7 hari kerja kemudian. Ia melampirkan persetujuan dari Atasan Langsungnya.

Service Desk menerima tiket, memverifikasi bahwa pengajuan dilakukan lebih dari 5 hari kerja sebelum tanggal kebutuhan, dan mengklasifikasikannya sebagai P3. Tiket diteruskan ke unit pengadaan untuk pemenuhan. Laptop tersedia dan diserahkan kepada pemohon pada tanggal 12 Juli, dua hari sebelum tanggal kebutuhan yang diminta.

Sebagai kontras, seandainya karyawan yang sama memerlukan laptop di hari yang sama pada tanggal 5 Juli, permintaannya akan ditolak karena tidak memenuhi satu pun dari ketiga syarat pengecualian permintaan di hari yang sama: bukan risiko keselamatan, bukan pemulihan insiden P1, dan bukan hari pertama kerja dengan kesalahan onboarding.

## Kebijakan Data, Kerahasiaan, dan Batas Layanan

### Prinsip Data Minimum

Setiap tiket yang dicatat di Service Portal hanya boleh memuat informasi bisnis minimum yang benar-benar diperlukan untuk memproses permintaan. Informasi yang dicantumkan harus relevan dengan jenis permintaan, proporsional terhadap kebutuhan penyelesaian, dan terbatas pada konteks operasional. Pemohon, Atasan Langsung, Service Desk, dan seluruh pihak yang menambahkan informasi ke dalam tiket bertanggung jawab secara individu untuk memastikan bahwa data yang mereka masukkan tidak melampaui kebutuhan operasional yang sah.

Prinsip data minimum berlaku pada setiap tahap siklus hidup tiket, mulai dari pencatatan awal hingga penutupan. Informasi yang tidak relevan dengan penyelesaian permintaan tidak boleh ditambahkan pada tahap mana pun. Service Desk berwenang menghapus informasi yang melanggar prinsip ini dan mencatat tindakan penghapusan dalam riwayat tiket.

### Data yang Dilarang dalam Tiket

Untuk melindungi kerahasiaan data dan mematuhi kebijakan keamanan informasi NusantaraCare, jenis data berikut tidak boleh ditempelkan, diketikkan, diunggah sebagai lampiran, atau diungkapkan dalam bentuk apa pun di dalam tiket Service Portal.

Pertama, informasi kesehatan pribadi dalam bentuk apa pun, termasuk tetapi tidak terbatas pada diagnosis medis, riwayat penyakit atau pengobatan, hasil pemeriksaan laboratorium, klaim asuransi kesehatan, dan surat keterangan dokter. Kedua, rincian perbankan dan keuangan pribadi seperti nomor rekening bank, nomor kartu kredit atau debit, informasi dompet digital, dan data keuangan pribadi lainnya. Ketiga, kata sandi, kode MFA, kunci API, token akses, sertifikat digital, dan segala bentuk kredensial autentikasi. Keempat, ekspor data pelanggan NusantaraCare, termasuk data transaksi, data kontak, data demografi, atau segala bentuk data yang dapat mengidentifikasi pelanggan secara individu. Kelima, system prompt, instruksi model, parameter konfigurasi internal, atau informasi teknis apa pun yang berkaitan dengan sistem kecerdasan buatan yang dioperasikan oleh NusantaraCare.

Pelanggaran terhadap larangan ini, baik yang disengaja maupun yang terjadi karena kelalaian, akan ditangani sebagai insiden keamanan. Tiket yang mengandung data terlarang akan segera dirutekan kepada Tim Keamanan Informasi dengan prioritas P1. Data terlarang yang ditemukan dalam tiket akan dihapus, dan apabila data tersebut bersifat kredensial, kredensial yang terkait wajib segera dinonaktifkan dan diganti.

### Permintaan Informasi Tiket Karyawan Lain

Permintaan untuk mengakses, melihat, atau mengetahui status atau isi tiket milik karyawan lain hanya dapat dipenuhi apabila pemohon memenuhi dua syarat kumulatif. Syarat pertama: pemohon memiliki kebutuhan operasional yang terdokumentasi secara tertulis, misalnya dalam rangka audit internal yang sah, investigasi insiden yang melibatkan karyawan tersebut, atau keperluan penggantian sementara tugas yang telah disetujui. Syarat kedua: pemohon telah mendapatkan persetujuan tertulis dari Pemilik Layanan yang membawahi sistem atau data yang terkait dengan tiket tersebut.

Service Desk wajib memverifikasi kelengkapan dokumentasi kebutuhan operasional dan keabsahan persetujuan Pemilik Layanan sebelum memberikan akses atau informasi apa pun. Dokumentasi dan persetujuan tersebut wajib dicatat dalam tiket sebagai bagian dari jejak audit. Keingintahuan pribadi, permintaan lisan tanpa dokumentasi, atau alasan kenyamanan administratif tidak termasuk kebutuhan operasional yang sah dan akan ditolak.

### Pelaporan Kecurigaan Keamanan

Setiap karyawan NusantaraCare yang mencurigai atau mengamati adanya potensi pelanggaran data, akses tidak sah ke sistem atau data, perubahan data yang tidak wajar atau tidak dikenal, pengiriman data ke pihak eksternal tanpa otorisasi, atau aktivitas lain yang mengindikasikan kemungkinan insiden keamanan informasi, wajib segera melaporkannya melalui Service Portal dengan memilih kategori keamanan atau insiden keamanan.

Laporan kecurigaan keamanan otomatis diklasifikasikan sebagai P1 dan dirutekan kepada Tim Keamanan Informasi tanpa penundaan, tanpa memerlukan verifikasi, persetujuan, atau penilaian dari Service Desk atau pihak lain. Service Desk tidak diperkenankan melakukan penyaringan, menunda, atau menilai validitas laporan kecurigaan keamanan sebelum meneruskannya. Kebijakan ini memastikan bahwa setiap potensi insiden keamanan mendapat perhatian segera dari tim yang berwenang.

Pemohon pelapor tidak perlu membuktikan kebenaran kecurigaannya. Niat baik dalam melaporkan kecurigaan dilindungi, dan pelapor tidak akan dikenai sanksi atas laporan yang diajukan dengan itikad baik meskipun investigasi kemudian menyimpulkan bahwa tidak terjadi insiden keamanan.

## Status Tiket, SLA, dan Komunikasi Pemohon

### Daftar Status Tiket dan Transisi

Setiap tiket dalam sistem Service Portal memiliki tepat satu status pada setiap waktu yang menggambarkan posisinya dalam alur kerja. Terdapat enam status yang diakui, dan setiap transisi antar-status mengikuti aturan yang ditetapkan di bawah.

Status Baru adalah status awal tiket yang baru dicatat dan belum ditinjau Service Desk. Service Desk wajib meninjau tiket Baru dalam batas waktu pengakuan sesuai prioritasnya, kemudian memindahkan ke Menunggu Persetujuan jika memerlukan persetujuan, atau langsung ke Sedang Diproses jika tidak. Status Menunggu Persetujuan menandakan tiket menunggu respons dari Atasan Langsung, Pemilik Layanan, atau pemberi persetujuan lain; tiket tetap dalam status ini hingga seluruh persetujuan diterima. Status Sedang Diproses menandakan penanganan teknis atau administratif sedang berlangsung; jika Service Desk memerlukan informasi tambahan, tiket berpindah ke Menunggu Pemohon. Status Selesai menandakan seluruh langkah penyelesaian telah dilaksanakan dan harus disertai ringkasan penyelesaian. Status Ditutup adalah status akhir yang tidak dapat diubah; tiket berpindah dari Selesai ke Ditutup secara otomatis setelah 5 hari kerja tanpa permintaan pembukaan kembali.

### Ketentuan Khusus Status Menunggu Pemohon

Status Menunggu Pemohon memiliki batas waktu yang ketat untuk mencegah tiket menggantung tanpa penyelesaian. Apabila pemohon tidak memberikan respons dalam waktu 3 hari kerja sejak tiket memasuki status Menunggu Pemohon, Service Desk akan menutup tiket secara otomatis dengan status Ditutup dan catatan bahwa tiket ditutup karena tidak ada respons dari pemohon.

Pemohon yang masih memerlukan penyelesaian untuk permasalahan yang sama dapat mengajukan permintaan pembukaan kembali tiket. Permintaan pembukaan kembali hanya dapat diajukan dalam waktu 5 hari kerja setelah tiket ditutup. Apabila disetujui, tiket kembali ke status sebelumnya sebelum Menunggu Pemohon. Permintaan pembukaan kembali yang diajukan setelah 5 hari kerja sejak penutupan tidak dapat dipenuhi, dan pemohon wajib membuat tiket baru untuk permasalahan yang sama.

### Persyaratan Status Selesai

Sebelum memindahkan tiket ke status Selesai, Service Desk atau Pemilik Layanan yang bertanggung jawab atas penyelesaian wajib menuliskan ringkasan penyelesaian yang memuat dua komponen: uraian tindakan yang diambil untuk menyelesaikan permintaan atau memulihkan layanan, dan langkah selanjutnya yang perlu dilakukan oleh pemohon apabila ada, misalnya melakukan pengecekan, mengonfirmasi penerimaan, atau mengatur ulang konfigurasi.

Ringkasan penyelesaian menjadi catatan permanen dalam riwayat tiket dan berfungsi sebagai acuan apabila permasalahan yang sama atau serupa muncul di kemudian hari, serta sebagai dasar untuk analisis tren dan peningkatan layanan. Tiket yang dipindahkan ke status Selesai tanpa ringkasan penyelesaian dianggap belum memenuhi standar operasional. Pemohon yang menerima tiket Selesai tanpa ringkasan penyelesaian yang memadai berhak mengajukan pembukaan kembali dalam masa 5 hari kerja dengan alasan ketidaklengkapan dokumentasi penyelesaian.

### Komunikasi Pemohon

Seluruh komunikasi antara Service Desk, pemohon, Atasan Langsung, Pemilik Layanan, dan pihak terkait lainnya wajib dilakukan melalui Service Portal dan tercatat sebagai bagian dari riwayat tiket. Komunikasi di luar portal, termasuk email pribadi, pesan instan, atau percakapan lisan, tidak memiliki kekuatan operasional, tidak dapat dijadikan bukti pemenuhan SLA atau dasar keluhan, dan tidak mengikat Service Desk.

Pemohon dapat melihat status terkini, riwayat lengkap, dan seluruh komunikasi pada tiketnya setiap saat melalui portal tanpa perlu menghubungi Service Desk secara langsung. Kemampuan pemantauan mandiri ini dimaksudkan untuk mengurangi beban pertanyaan status kepada Service Desk dan memberikan transparansi penuh kepada pemohon.

## FAQ Operasional

### Pertanyaan Saluran Layanan

**T: Apakah saya bisa mengirim permintaan melalui WhatsApp ke petugas Service Desk?**
J: Tidak. WhatsApp, Telegram, dan seluruh aplikasi percakapan instan bukan saluran resmi Service Desk. Seluruh permintaan wajib disampaikan melalui Service Portal. Permintaan melalui saluran tidak resmi tidak akan diproses dan tidak mengikat Service Desk.

**T: Kapan saya boleh menggunakan email untuk melaporkan gangguan?**
J: Email servicedesk@nusantaracare.internal hanya dapat digunakan saat Service Portal tidak tersedia atau tidak dapat diakses. Subjek email wajib diawali [DARURAT-PORTAL]. Email tanpa penanda atau saat portal normal tidak akan diproses. Setelah portal kembali tersedia, Anda tetap wajib membuat tiket di portal.

### Pertanyaan Prioritas dan SLA

**T: Bagaimana cara agar tiket saya diprioritaskan menjadi P1?**
J: Prioritas tiket tidak dapat diminta atau dinegosiasikan oleh pemohon. Service Desk menetapkan prioritas secara objektif berdasarkan dua kriteria: dampak dan urgensi. Sebuah tiket hanya diklasifikasikan sebagai P1 apabila memenuhi kriteria dampak, yaitu gangguan berdampak pada lebih dari 25 karyawan secara bersamaan, atau kriteria keamanan, yaitu terdapat indikasi atau kecurigaan insiden data atau keamanan. Jabatan, senioritas, atau preferensi pemohon tidak memengaruhi penetapan prioritas. Jika situasi memburuk setelah tiket dibuat, Service Desk dapat menaikkan prioritas berdasarkan kondisi terbaru.

**T: Tiket P2 saya belum ada perkembangan setelah 3 jam. Apakah ini wajar?**
J: Ya, ini wajar. Tiket P2 mendapatkan pembaruan status satu kali per hari kerja. Service Desk tidak memberikan pembaruan di antara jadwal tersebut kecuali terjadi perubahan status yang signifikan, misalnya ditemukannya workaround atau penyelesaian. Waktu pengakuan tiket P2 adalah 4 jam kerja, dan waktu penyelesaian bergantung pada kompleksitas permasalahan. Anda dapat memantau status tiket Anda setiap saat melalui Service Portal tanpa perlu menunggu pembaruan dari Service Desk.

### Pertanyaan Akses

**T: Persetujuan siapa saja yang saya perlukan untuk mendapatkan akses ke aplikasi baru?**
J: Anda memerlukan dua persetujuan yang keduanya wajib dipenuhi. Pertama, persetujuan dari Atasan Langsung Anda yang memverifikasi bahwa akses tersebut sesuai dengan kebutuhan dan tanggung jawab pekerjaan Anda. Kedua, persetujuan dari Pemilik Layanan aplikasi yang Anda minta aksesnya. Service Desk hanya dapat memproses provisioning setelah kedua persetujuan tersebut diterima dan tercatat dalam sistem. Tanpa kedua persetujuan lengkap, permintaan akses Anda tidak dapat diproses.

**T: Saya lupa kata sandi aplikasi. Apakah saya bisa memintanya melalui tiket?**
J: Tidak, dan ini adalah larangan mutlak. Kata sandi, kode MFA, kunci API, dan segala bentuk kredensial tidak boleh diminta, dituliskan, atau dikirimkan melalui tiket dalam bentuk apa pun. Melanggar larangan ini akan dicatat sebagai insiden keamanan. Untuk mengatasi lupa kata sandi, gunakan mekanisme reset kata sandi yang disediakan oleh masing-masing aplikasi. Jika mekanisme reset tidak tersedia atau tidak berfungsi, buat tiket untuk meminta bantuan reset tanpa menyertakan kata sandi apa pun.

**T: Berapa lama akses sementara dapat diberikan? Bisa diperpanjang?**
J: Akses sementara diberikan untuk durasi maksimal 14 hari kalender sejak tanggal aktivasi. Saat mengajukan, Anda wajib mencantumkan tanggal kedaluwarsa yang jelas. Tidak ada mekanisme perpanjangan otomatis. Jika Anda memerlukan akses lebih lama, Anda wajib mengajukan permintaan akses baru melalui Service Portal sebelum tanggal kedaluwarsa akses yang sedang berjalan. Permintaan perpanjangan diperlakukan sebagai permintaan baru dan memerlukan persetujuan lengkap dari Atasan Langsung dan Pemilik Layanan seperti permintaan awal.

### Pertanyaan Gangguan

**T: Saya sudah melaporkan gangguan sistem. Kapan tepatnya layanan akan pulih?**
J: Service Desk tidak dapat memberikan estimasi waktu pemulihan sebelum mendapatkan konfirmasi resmi dari Pemilik Layanan dari sistem yang terdampak. Kebijakan ini mencegah penyampaian informasi yang belum terverifikasi kepada pemohon. Setelah Pemilik Layanan memberikan konfirmasi estimasi waktu pemulihan, Service Desk akan segera menyampaikannya kepada Anda melalui pembaruan tiket di portal. Sementara menunggu konfirmasi, Service Desk akan memberikan pembaruan berkala sesuai prioritas tiket Anda.

**T: Apa yang harus saya lakukan jika saya mencurigai adanya pelanggaran keamanan data?**
J: Segera buka tiket di Service Portal dan pilih kategori keamanan atau insiden keamanan. Laporan Anda akan otomatis diklasifikasikan sebagai P1 dan dirutekan langsung kepada Tim Keamanan Informasi tanpa penundaan, tanpa memerlukan verifikasi atau persetujuan dari Service Desk. Anda tidak perlu membuktikan kebenaran kecurigaan Anda. Sampaikan semua informasi yang Anda ketahui: apa yang Anda amati, kapan, sistem apa yang terlibat, dan siapa saja yang mungkin terkait. Niat baik Anda dalam melaporkan dilindungi oleh kebijakan perusahaan.

### Pertanyaan Perlengkapan

**T: Saya memerlukan keyboard baru. Kapan paling lambat saya harus mengajukan permintaan?**
J: Permintaan perlengkapan standar seperti keyboard, mouse, headset, atau monitor wajib diajukan melalui Service Portal minimal 5 hari kerja sebelum tanggal Anda memerlukan perlengkapan tersebut. Pengajuan harus disertai persetujuan dari Atasan Langsung Anda. Jika Anda mengajukan kurang dari 5 hari kerja sebelum tanggal kebutuhan, Service Desk tetap akan memproses permintaan Anda, tetapi pemenuhan pada tanggal yang diminta tidak dapat dijamin, kecuali permintaan Anda memenuhi syarat pengecualian permintaan di hari yang sama.

**T: Keyboard saya rusak hari ini dan saya tidak bisa mengetik. Apakah saya bisa langsung minta penggantian di hari yang sama?**
J: Penggantian di hari yang sama hanya dapat dipenuhi jika kerusakan keyboard Anda memenuhi salah satu dari tiga syarat pengecualian: menimbulkan risiko keselamatan; merupakan bagian dari pemulihan insiden P1 yang sedang berlangsung; atau Anda sedang menjalani hari pertama kerja dan kegagalan penyediaan disebabkan oleh kesalahan onboarding yang terdokumentasi. Jika kerusakan keyboard Anda tidak memenuhi ketiga syarat tersebut, laporkan sebagai insiden melalui portal dan ajukan penggantian dengan tenggat 5 hari kerja.

### Pertanyaan Kerahasiaan

**T: Rekan satu tim saya sedang cuti dan ada tiketnya yang perlu saya ketahui statusnya. Bolehkah saya menanyakan status tiket tersebut?**
J: Anda hanya dapat menanyakan atau mengakses informasi tiket karyawan lain jika memenuhi dua syarat kumulatif. Pertama, Anda memiliki kebutuhan operasional yang terdokumentasi secara tertulis, misalnya surat penugasan yang menyebutkan bahwa Anda mengambil alih tanggung jawab rekan Anda selama masa cuti. Kedua, Anda telah mendapatkan persetujuan tertulis dari Pemilik Layanan yang membawahi sistem atau data terkait tiket tersebut. Service Desk wajib memverifikasi kedua syarat ini sebelum memberikan informasi apa pun. Tanpa dokumentasi dan persetujuan yang lengkap, permintaan Anda akan ditolak demi menjaga kerahasiaan data setiap karyawan.

## Lampiran Matriks Keputusan

### Matriks Prioritas

| Prioritas | Kriteria Dampak | Target Pengakuan | Frekuensi Pembaruan | Eskalasi |
| --- | --- | --- | --- | --- |
| P1 | Lebih dari 25 karyawan terdampak secara bersamaan, atau terdapat indikasi insiden data atau keamanan | 30 menit sejak pencatatan | Setiap 30 menit selama insiden berlangsung | Notifikasi segera ke Manajer Piket; eskalasi penuh setelah 60 menit tanpa workaround |
| P2 | Pekerjaan pemohon terhambat signifikan dan tidak tersedia workaround yang telah disetujui | 4 jam kerja sejak pencatatan | Satu kali per hari kerja | Kepada Pemilik Layanan jika memerlukan keahlian atau akses teknis spesifik |
| P3 | Permintaan normal, memiliki workaround yang disetujui, atau tenggat masih jauh | 1 hari kerja sejak pencatatan | Saat status berubah secara signifikan | Tidak ada eskalasi rutin; dapat dieskalasi jika situasi berubah |

### Matriks Pemilihan Jalur

| Situasi | Saluran yang Benar | Persetujuan Wajib | Target SLA | Acuan SOP |
| --- | --- | --- | --- | --- |
| Akses aplikasi baru | Service Portal | Atasan Langsung dan Pemilik Layanan | Provisioning dalam 2 hari kerja setelah kedua persetujuan diterima | SOP Permintaan Akses dan Akun |
| Akses sementara (maks. 14 hari) | Service Portal | Atasan Langsung | Provisioning dalam 2 hari kerja; wajib mencantumkan tanggal kedaluwarsa | SOP Permintaan Akses dan Akun |
| Gangguan atau insiden P1 | Service Portal dan telepon | Tidak ada (otomatis P1 berdasarkan kriteria) | Pengakuan 30 menit, pembaruan setiap 30 menit, penanganan 24/7 | SOP Gangguan Layanan dan Eskalasi |
| Permintaan perlengkapan standar | Service Portal | Atasan Langsung | Pengajuan minimal 5 hari kerja sebelum tanggal kebutuhan | SOP Fasilitas dan Perlengkapan Kerja |
| Peralatan hilang atau rusak | Service Portal (kategori insiden) | Atasan Langsung (untuk penggantian) | Diproses sesuai prioritas; umumnya P3 kecuali memicu P1 atau P2 | SOP Fasilitas dan Perlengkapan Kerja |

Kedua matriks di atas merupakan ringkasan referensi cepat untuk penggunaan harian. Matriks ini tidak menggantikan ketentuan lengkap dalam teks SOP. Untuk prosedur rinci, ketentuan pengecualian, tanggung jawab setiap peran, dan contoh penerapan, selalu rujuk ke bagian SOP terkait di dalam panduan ini. Apabila terdapat perbedaan penafsiran antara matriks ringkas dan teks SOP, ketentuan yang tercantum dalam teks SOP yang berlaku sebagai acuan utama.

## Riwayat Perubahan dan Arsip Kebijakan

Panduan Operasional Layanan Internal NusantaraCare versi 2.0 berlaku efektif sejak 1 Juli 2026 dan menggantikan seluruh versi sebelumnya, termasuk versi 1.4 dan seluruh revisi minor di antaranya. Versi ini diterbitkan oleh Direktorat Operasi dan Layanan Internal dan merupakan satu-satunya acuan yang sah untuk seluruh keputusan operasional mulai tanggal efektif tersebut. Setiap ketentuan dalam versi sebelumnya yang bertentangan dengan versi 2.0 dinyatakan tidak berlaku.

### Arsip Kebijakan v1.4 — NONAKTIF

Versi 1.4 berlaku 1 Januari 2025 hingga 30 Juni 2026, kini berstatus tidak aktif dan tidak boleh digunakan untuk keputusan operasional. Dua ketentuan utama v1.4 yang berbeda dari v2.0: pertama, v1.4 mengizinkan pengiriman permintaan melalui email biasa sebagai saluran setara dengan Service Portal, tanpa penanda [DARURAT-PORTAL] dan tanpa syarat portal harus tidak tersedia; kedua, v1.4 menetapkan batas pengajuan permintaan perlengkapan kerja minimal 3 hari kerja sebelum tanggal kebutuhan.

Kedua ketentuan tersebut tidak berlaku sejak 1 Juli 2026. Metadata arsip: `is_active: false`, `effective_date: 2025-01-01`, `effective_until: 2026-06-30`.

### Pengganti Aktif v2.0

Ketentuan saluran pengganti: lihat [Kanal Layanan dan Waktu Operasional](#kanal-layanan-dan-waktu-operasional). Saluran v2.0: Service Portal untuk seluruh permintaan, telepon untuk P1, dan email [DARURAT-PORTAL] hanya saat portal tidak tersedia atau tidak dapat diakses. WhatsApp, pesan pribadi, dan saluran tidak resmi tidak diakui.

Ketentuan perlengkapan pengganti: lihat [SOP Fasilitas dan Perlengkapan Kerja](#sop-fasilitas-dan-perlengkapan-kerja). Pengajuan minimal 5 hari kerja, bukan 3 hari kerja seperti v1.4. Pengecualian hari yang sama hanya diberikan untuk risiko keselamatan, pemulihan insiden P1, atau hari pertama kerja dengan kesalahan onboarding yang terdokumentasi, dan wajib mendapat persetujuan Manajer Piket.
