#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "Chris Griffith"
from pathlib import Path

import pkg_resources

name = "AV1 (AOM)"
requires = "libaom"
icon = str(Path(pkg_resources.resource_filename(__name__, f"../../data/encoders/icon_av1_aom.png")).resolve())

video_extension = "mkv"
video_dimension_divisor = 8

enable_subtitles = True
enable_audio = True
enable_attachments = True

audio_formats = [
    "aac",
    "ac3",
    "dts",
    "truehd",
    "flac",
    "vorbis",
    "libvorbis",
    "opus",
    "libopus",
    "acm",
    "tta",
    "wavpack",
    "ac3_fixed",
    "alac",
    "dca",
    "pcm_dvd",
    "pcm_f32be",
    "pcm_f32le",
    "pcm_f64be",
    "pcm_f64le",
    "pcm_mulaw",
    "pcm_s16be",
    "pcm_s16be_planar",
    "pcm_s16le",
    "pcm_s16le_planar",
    "pcm_s24be",
    "pcm_s24daud",
    "pcm_s24le",
    "pcm_s24le_planar",
    "pcm_s32be",
    "pcm_s32le",
    "pcm_s32le_planar",
    "pcm_s64be",
    "pcm_s64le",
    "pcm_s8",
    "pcm_s8_planar",
    "pcm_u16be",
    "pcm_u16le",
    "pcm_u24be",
    "pcm_u24le",
    "pcm_u32be",
    "pcm_u32le",
    "pcm_u8",
]

from fastflix.encoders.av1_aom.command_builder import build
from fastflix.encoders.av1_aom.settings_panel import AV1 as settings_panel
