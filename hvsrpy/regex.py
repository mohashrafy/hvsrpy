# This file is part of hvsrpy, a Python package for
# horizontal-to-vertical spectral ratio processing.
# Copyright (C) 2019-2022 Joseph P. Vantassel (joseph.p.vantassel@gmail.com)
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https: //www.gnu.org/licenses/>.

"""Regular expressions for text parsing."""

import re

NEWLINE = r"[\r\n?|\n]"

# DataWrangler | saf
# ------------------
saf_npts_expr = f"NDAT = (\d+){NEWLINE}"
saf_fs_expr = f"SAMP_FREQ = (\d+){NEWLINE}"
saf_sample_expr = "-?\d+" 
saf_row_expr = f"^({saf_sample_expr})\s({saf_sample_expr})\s({saf_sample_expr}){NEWLINE}"
saf_v_ch_expr = f"CH(\d)_ID = V"
saf_n_ch_expr = f"CH(\d)_ID = N"
saf_e_ch_expr = f"CH(\d)_ID = E"
saf_north_rot_expr = "NORTH_ROT = (\d+)"
saf_version_expr = "SESAME ASCII data format \(saf\) v. (\d)"

saf_npts_exec = re.compile(saf_npts_expr)
saf_fs_exec = re.compile(saf_fs_expr)
saf_row_exec = re.compile(saf_row_expr, flags=re.MULTILINE)
saf_v_ch_exec = re.compile(saf_v_ch_expr)
saf_n_ch_exec = re.compile(saf_n_ch_expr)
saf_e_ch_exec = re.compile(saf_e_ch_expr)
saf_north_rot_exec = re.compile(saf_north_rot_expr)
saf_version_exec = re.compile(saf_version_expr)


# DataWrangler | minishark
# ------------------------
mshark_npts_expr = f"#Sample number:\t(\d+){NEWLINE}"
mshark_fs_expr = f"#Sample rate \(sps\):\t(\d+){NEWLINE}"
mshark_gain_expr = f"#Gain:\t(\d+){NEWLINE}"
mshark_conversion_expr = f"#Conversion factor:\t(\d+){NEWLINE}"
mshark_sample_expr = "-?\d+" 
mshark_row_expr = f"({mshark_sample_expr})\t({mshark_sample_expr})\t({mshark_sample_expr}){NEWLINE}"

mshark_npts_exec = re.compile(mshark_npts_expr)
mshark_fs_exec = re.compile(mshark_fs_expr)
mshark_gain_exec = re.compile(mshark_gain_expr)
mshark_conversion_exec = re.compile(mshark_conversion_expr)
mshark_row_exec = re.compile(mshark_row_expr)

# DataWrangler | peer
# -------------------
peer_direction_expr = f", (UP|\d|\d\d|\d\d\d|[FGDCESHB][HLGMN][ENZ]){NEWLINE}" 
peer_npts_expr = "NPTS=\s*(\d+),"
peer_dt_expr = f"DT=\s*(\d*\.\d+)\s"
peer_sample_expr = "(-?\.\d+E[+-]?\d*)"

peer_direction_exec = re.compile(peer_direction_expr)
peer_npts_exec = re.compile(peer_npts_expr)
peer_dt_exec = re.compile(peer_dt_expr)
peer_sample_exec = re.compile(peer_sample_expr)
