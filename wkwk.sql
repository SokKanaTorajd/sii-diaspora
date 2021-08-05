-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 06, 2021 at 03:45 PM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.2.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wkwk`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `kd_admin` char(10) NOT NULL,
  `nm_lengkap` varchar(25) NOT NULL,
  `alamat` varchar(35) NOT NULL,
  `notlp` varchar(15) NOT NULL,
  `username` varchar(15) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`kd_admin`, `nm_lengkap`, `alamat`, `notlp`, `username`, `password`) VALUES
('01', 'Rifky Nur Febryan', 'Jl.Raya Pleret', '08763473', 'admin', 'admin');

-- --------------------------------------------------------

--
-- Table structure for table `barang`
--

CREATE TABLE `barang` (
  `kd_obat` char(10) NOT NULL,
  `nm_obat` varchar(25) NOT NULL,
  `jenis_obat` varchar(15) NOT NULL,
  `asal` varchar(225) NOT NULL,
  `tahun` int(10) NOT NULL,
  `stok` int(5) NOT NULL,
  `harga` int(225) NOT NULL,
  `tempat` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `barang`
--

INSERT INTO `barang` (`kd_obat`, `nm_obat`, `jenis_obat`, `asal`, `tahun`, `stok`, `harga`, `tempat`) VALUES
('02.01.06', 'Station Wagon', 'SUZUKI/APV GX M', 'Pembelian', 1998, 1, 79616000, 'Appk'),
('02.02.03', 'Mesin Ketik', 'Romington', 'Pembelian', 1971, 2, 300000, 'BANGDES'),
('02.03.01.0', 'Minibus', 'Toyota/All new ', 'BM', 2013, 2, 1870000000, 'Kec. Kraton'),
('02.04.01', 'Sepeda Motor', 'SUZUKI/SMASH FI', 'Pembelian', 2002, 6, 13175000, 'Kantor'),
('02.05.01', 'Almari Besi Lereg Kaca', 'Brother/B-304', 'Pembelian', 2014, 1, 23000000, 'Kantor'),
('02.06.01.0', 'Almari Besi', 'Brother', 'Pembelian', 2018, 23, 3175000, 'BM Almari'),
('02.07.06', 'Rak Besi', '-', 'Pembelian', 1995, 1, 150000, 'Kantor'),
('02.08.02', 'FELING KABINET', 'ICHIBAN', 'Pembelian', 1996, 1, 500000, 'BANGDES'),
('02.09.03', 'FELING KABINET', 'VIP', 'Pembelian', 1998, 1, 650000, 'BANGDES'),
('03.01.02', 'feling kabinet', 'Royal', 'Pembelian', 1998, 1, 650000, 'Kantor'),
('03.03.07', 'Feling Kabinet', 'elit,batas krip', 'Pembelian', 2001, 4, 825000, 'Linmas,Bar'),
('03.04.03', 'Feling cabinet', 'Brother', 'Pembelian', 2008, 19, 1625000, 'BM Filling'),
('03.05.08', 'Feling cabinet', 'Brother/B-104', 'Pembelian', 2009, 1, 1275000, 'Kantor'),
('03.06.07', 'Feling cabinet', 'TOP/FCT 4 ', 'BM', 2013, 1, 1487200, 'Kantor Kes'),
('03.07.09', 'Lemari kayu 3 pintu dan 2', '-', 'Pembelian', 1987, 1, 200000, 'BANGDES');

-- --------------------------------------------------------

--
-- Table structure for table `barangnon`
--

CREATE TABLE `barangnon` (
  `kd_barangnon` varchar(10) NOT NULL,
  `nm_barangnon` varchar(25) NOT NULL,
  `jenis_barangnon` varchar(15) NOT NULL,
  `asal` varchar(225) NOT NULL,
  `tgl_masuk` date NOT NULL,
  `stok` int(5) NOT NULL,
  `harga` int(225) NOT NULL,
  `tempat` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `barangnon`
--

INSERT INTO `barangnon` (`kd_barangnon`, `nm_barangnon`, `jenis_barangnon`, `asal`, `tgl_masuk`, `stok`, `harga`, `tempat`) VALUES
('04.01.01', 'Bola Volly', 'MIZUNO', 'Pembelian', '2019-07-08', 5, 350000, 'Gudang'),
('04.02.03', 'Net Bola Volly', '-', 'Pembelian', '2019-07-08', 3, 485000, 'Gudang'),
('04.03.05', 'SAMSAK', '-', 'Pembelian', '2019-01-06', 5, 500000, 'Gudang');

-- --------------------------------------------------------

--
-- Table structure for table `eoq`
--

CREATE TABLE `eoq` (
  `id` int(10) NOT NULL,
  `kd_obat` char(10) NOT NULL,
  `kd_kondisi` varchar(10) NOT NULL,
  `barang_rusak` int(5) NOT NULL,
  `keterangan` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `eoq`
--

INSERT INTO `eoq` (`id`, `kd_obat`, `kd_kondisi`, `barang_rusak`, `keterangan`) VALUES
(18, '02.03.01.0', 'kdb2', 1, 'Harus Service'),
(19, '02.06.01.0', 'kdb1', 0, 'BM Almari');

-- --------------------------------------------------------

--
-- Table structure for table `eoqnon`
--

CREATE TABLE `eoqnon` (
  `idnon` int(10) NOT NULL,
  `kd_barangnon` varchar(10) NOT NULL,
  `kd_kondisi` varchar(10) NOT NULL,
  `tgl_keluar` date NOT NULL,
  `barang_keluar` int(5) NOT NULL,
  `keterangan` varchar(225) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `eoqnon`
--

INSERT INTO `eoqnon` (`idnon`, `kd_barangnon`, `kd_kondisi`, `tgl_keluar`, `barang_keluar`, `keterangan`) VALUES
(32, '05.18.02.0', 'kdb1', '0000-00-00', 0, '-'),
(33, '04.03.05', 'kdb1', '2019-08-29', 0, 'Digunakan Latihan PORDA JOGJA '),
(34, '04.02.03', 'kdb1', '2019-08-29', 0, 'Digunakan Latihan PORDA JOGJA '),
(35, '04.01.01', 'kdb1', '2019-08-29', 0, 'Digunakan Latihan PORDA JOGJA ');

-- --------------------------------------------------------

--
-- Table structure for table `kondisi`
--

CREATE TABLE `kondisi` (
  `kd_kondisi` varchar(10) NOT NULL,
  `kondisi` varchar(100) CHARACTER SET latin1 NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `kondisi`
--

INSERT INTO `kondisi` (`kd_kondisi`, `kondisi`) VALUES
('kdb1', 'Baik'),
('kdb2', 'Rusak Ringan'),
('kdb3', 'Rusak Berat'),
('kdb4', 'Harus di Ganti');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`kd_admin`);

--
-- Indexes for table `barang`
--
ALTER TABLE `barang`
  ADD PRIMARY KEY (`kd_obat`);

--
-- Indexes for table `barangnon`
--
ALTER TABLE `barangnon`
  ADD PRIMARY KEY (`kd_barangnon`);

--
-- Indexes for table `eoq`
--
ALTER TABLE `eoq`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `eoqnon`
--
ALTER TABLE `eoqnon`
  ADD PRIMARY KEY (`idnon`);

--
-- Indexes for table `kondisi`
--
ALTER TABLE `kondisi`
  ADD PRIMARY KEY (`kd_kondisi`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `eoq`
--
ALTER TABLE `eoq`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `eoqnon`
--
ALTER TABLE `eoqnon`
  MODIFY `idnon` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
