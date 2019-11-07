folder = """
#define folder_width 16
#define folder_height 16
static unsigned char folder_bits[] = {
   0x00, 0x00, 0x3f, 0x00, 0xf1, 0x7f, 0x01, 0x40, 0xfd, 0xff, 0x07, 0x80,
   0x03, 0x80, 0x03, 0x80, 0x03, 0x80, 0x03, 0x80, 0x01, 0xc0, 0x01, 0x40,
   0x01, 0x40, 0x01, 0x40, 0xfe, 0x7f, 0x00, 0x00 };
"""

folder_mask = """
#define folder_mask_width 16
#define folder_mask_height 16
static unsigned char folder_mask_bits[] = {
   0x00, 0x00, 0x3f, 0x00, 0xff, 0x7f, 0xff, 0x7f, 0xff, 0xff, 0xff, 0xff,
   0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0x7f,
   0xff, 0x7f, 0xff, 0x7f, 0xfe, 0x7f, 0x00, 0x00 };
"""

button_close = """
#define button_close_width 16
#define button_close_height 16
static unsigned char button_close_bits[] = {
   0x00, 0x00, 0x06, 0x60, 0x0e, 0x70, 0x1c, 0x38, 0x38, 0x1c, 0x70, 0x0e,
   0xe0, 0x07, 0x40, 0x02, 0x40, 0x02, 0xe0, 0x07, 0x70, 0x0e, 0x38, 0x1c,
   0x1c, 0x38, 0x0e, 0x70, 0x06, 0x60, 0x00, 0x00 };
"""

button_close_mask = """
#define button_close_mask_width 16
#define button_close_mask_height 16
static unsigned char button_close_mask_bits[] = {
   0x00, 0x00, 0x06, 0x60, 0x0e, 0x70, 0x1c, 0x38, 0x38, 0x1c, 0x70, 0x0e,
   0xe0, 0x07, 0x40, 0x02, 0x40, 0x02, 0xe0, 0x07, 0x70, 0x0e, 0x38, 0x1c,
   0x1c, 0x38, 0x0e, 0x70, 0x06, 0x60, 0x00, 0x00 };
"""

button_close_small = """
#define button_close_small_width 8
#define button_close_small_height 8
static unsigned char button_close_small_bits[] = {
   0x81, 0x42, 0x24, 0x18, 0x18, 0x24, 0x42, 0x81 };
"""

button_close_small_mask = """
#define button_close_small_mask_width 8
#define button_close_small_mask_height 8
static unsigned char button_close_small_mask_bits[] = {
   0x81, 0x42, 0x24, 0x18, 0x18, 0x24, 0x42, 0x81 };

"""

button_collapse_mask = """
#define button_collapse_mask_width 16
#define button_collapse_mask_height 16
static unsigned char button_collapse_mask_bits[] = {
   0x00, 0x00, 0xfe, 0x7f, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40,
   0x02, 0x40, 0xfa, 0x5f, 0xfa, 0x5f, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40,
   0x02, 0x40, 0x02, 0x40, 0xfe, 0x7f, 0x00, 0x00 };
"""

button_collapse = """
#define button_collapse_width 16
#define button_collapse_height 16
static unsigned char button_collapse_bits[] = {
   0x00, 0x00, 0xfe, 0x7f, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40,
   0x02, 0x40, 0xfa, 0x5f, 0xfa, 0x5f, 0x02, 0x40, 0x02, 0x40, 0x02, 0x40,
   0x02, 0x40, 0x02, 0x40, 0xfe, 0x7f, 0x00, 0x00 };
"""

button_open_mask = """
#define button_open_mask_width 16
#define button_open_mask_height 16
static unsigned char button_open_mask_bits[] = {
   0x00, 0x00, 0xfe, 0x7f, 0x02, 0x40, 0x82, 0x41, 0x82, 0x41, 0x82, 0x41,
   0x82, 0x41, 0xfa, 0x5f, 0xfa, 0x5f, 0x82, 0x41, 0x82, 0x41, 0x82, 0x41,
   0x82, 0x41, 0x02, 0x40, 0xfe, 0x7f, 0x00, 0x00 };

"""

button_open = """
#define button_open_width 16
#define button_open_height 16
static unsigned char button_open_bits[] = {
   0x00, 0x00, 0xfe, 0x7f, 0x02, 0x40, 0x82, 0x41, 0x82, 0x41, 0x82, 0x41,
   0x82, 0x41, 0xfa, 0x5f, 0xfa, 0x5f, 0x82, 0x41, 0x82, 0x41, 0x82, 0x41,
   0x82, 0x41, 0x02, 0x40, 0xfe, 0x7f, 0x00, 0x00 };
"""

button_pause_mask = """
#define button_pause_mask_width 16
#define button_pause_mask_height 16
static unsigned char button_pause_mask_bits[] = {
   0x00, 0x00, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c,
   0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c,
   0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x00, 0x00 };
"""

button_pause = """
#define button_pause_width 16
#define button_pause_height 16
static unsigned char button_pause_bits[] = {
   0x00, 0x00, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c,
   0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c,
   0x60, 0x0c, 0x60, 0x0c, 0x60, 0x0c, 0x00, 0x00 };
"""

button_play_mask = """
#define button_play_mask_width 16
#define button_play_mask_height 16
static unsigned char button_play_mask_bits[] = {
   0x00, 0x00, 0x10, 0x00, 0x30, 0x00, 0x70, 0x00, 0xf0, 0x00, 0xf0, 0x01,
   0xf0, 0x03, 0xf0, 0x07, 0xf0, 0x07, 0xf0, 0x03, 0xf0, 0x01, 0xf0, 0x00,
   0x70, 0x00, 0x30, 0x00, 0x10, 0x00, 0x00, 0x00 };
"""

button_play = """
#define button_play_width 16
#define button_play_height 16
static unsigned char button_play_bits[] = {
   0x00, 0x00, 0x10, 0x00, 0x30, 0x00, 0x70, 0x00, 0xf0, 0x00, 0xf0, 0x01,
   0xf0, 0x03, 0xf0, 0x07, 0xf0, 0x07, 0xf0, 0x03, 0xf0, 0x01, 0xf0, 0x00,
   0x70, 0x00, 0x30, 0x00, 0x10, 0x00, 0x00, 0x00 };
"""

button_stop_mask = """
#define button_stop_mask_width 16
#define button_stop_mask_height 16
static unsigned char button_stop_mask_bits[] = {
   0x00, 0x00, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f,
   0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f,
   0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0x00, 0x00 };
"""

button_stop = """
#define button_stop_width 16
#define button_stop_height 16
static unsigned char button_stop_bits[] = {
   0x00, 0x00, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f,
   0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f,
   0xfe, 0x7f, 0xfe, 0x7f, 0xfe, 0x7f, 0x00, 0x00 };
"""

imagefile_mask = """
#define imagefile_mask_width 16
#define imagefile_mask_height 16
static unsigned char imagefile_mask_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xfc, 0x3f, 0x02, 0x40, 0x22, 0x4c, 0x72, 0x52,
   0xfa, 0x52, 0x02, 0x4c, 0x02, 0x40, 0xfa, 0x40, 0x8a, 0x40, 0xfa, 0x40,
   0x02, 0x40, 0xfc, 0x3f, 0x00, 0x00, 0x00, 0x00 };
"""

imagefile = """
#define imagefile_width 16
#define imagefile_height 16
static unsigned char imagefile_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xfc, 0x3f, 0x02, 0x40, 0x22, 0x4c, 0x72, 0x52,
   0xfa, 0x52, 0x02, 0x4c, 0x02, 0x40, 0xfa, 0x40, 0x8a, 0x40, 0xfa, 0x40,
   0x02, 0x40, 0xfc, 0x3f, 0x00, 0x00, 0x00, 0x00 };
"""

moviefile_mask = """
#define moviefile_mask_width 16
#define moviefile_mask_height 16
static unsigned char moviefile_mask_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xfc, 0x7f, 0x02, 0x80, 0x0a, 0xb6, 0x1a, 0xb6,
   0x3a, 0xb6, 0x7a, 0xb6, 0x3a, 0xb6, 0x1a, 0xb6, 0x0a, 0xb6, 0x02, 0x80,
   0xfc, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
"""

moviefile = """
#define moviefile_width 16
#define moviefile_height 16
static unsigned char moviefile_bits[] = {
   0x00, 0x00, 0x00, 0x00, 0xfc, 0x7f, 0x02, 0x80, 0x0a, 0xb6, 0x1a, 0xb6,
   0x3a, 0xb6, 0x7a, 0xb6, 0x3a, 0xb6, 0x1a, 0xb6, 0x0a, 0xb6, 0x02, 0x80,
   0xfc, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
"""

musicfile_mask = """
#define musicfile_mask_width 16
#define musicfile_mask_height 16
static unsigned char musicfile_mask_bits[] = {
   0x00, 0x1e, 0x00, 0x19, 0xc0, 0x16, 0x30, 0x11, 0xd0, 0x10, 0x30, 0x10,
   0x10, 0x10, 0x10, 0x10, 0x10, 0x0e, 0x10, 0x1f, 0x10, 0x1f, 0x0e, 0x1f,
   0x1f, 0x0e, 0x1f, 0x00, 0x1f, 0x00, 0x0e, 0x00 };
"""

musicfile = """
#define musicfile_width 16
#define musicfile_height 16
static unsigned char musicfile_bits[] = {
   0x00, 0x1e, 0x00, 0x19, 0xc0, 0x16, 0x30, 0x11, 0xd0, 0x10, 0x30, 0x10,
   0x10, 0x10, 0x10, 0x10, 0x10, 0x0e, 0x10, 0x1f, 0x10, 0x1f, 0x0e, 0x1f,
   0x1f, 0x0e, 0x1f, 0x00, 0x1f, 0x00, 0x0e, 0x00 };
"""

textfile_mask = """
#define textfile_mask_width 16
#define textfile_mask_height 16
static unsigned char textfile_mask_bits[] = {
   0x00, 0x00, 0xfc, 0x3f, 0x06, 0x48, 0x06, 0x50, 0xf6, 0x67, 0x06, 0x60,
   0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40, 0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40,
   0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40, 0xfc, 0x3f };
"""

textfile = """
#define textfile_width 16
#define textfile_height 16
static unsigned char textfile_bits[] = {
   0x00, 0x00, 0xfc, 0x3f, 0x06, 0x48, 0x06, 0x50, 0xf6, 0x67, 0x06, 0x60,
   0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40, 0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40,
   0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40, 0xfc, 0x3f };
"""

volume_icon_mask = """
#define volume_icon_mask_width 16
#define volume_icon_mask_height 16
static unsigned char volume_icon_mask_bits[] = {
   0x00, 0x00, 0x00, 0x10, 0x40, 0x20, 0x60, 0x20, 0x60, 0x44, 0x70, 0x48,
   0x78, 0x89, 0x7e, 0x92, 0x7e, 0x92, 0x78, 0x89, 0x70, 0x48, 0x60, 0x44,
   0x60, 0x20, 0x40, 0x20, 0x00, 0x10, 0x00, 0x00 };
"""

volume_icon = """
#define volume_icon_width 16
#define volume_icon_height 16
static unsigned char volume_icon_bits[] = {
   0x00, 0x00, 0x00, 0x10, 0x40, 0x20, 0x60, 0x20, 0x60, 0x44, 0x70, 0x48,
   0x78, 0x89, 0x7e, 0x92, 0x7e, 0x92, 0x78, 0x89, 0x70, 0x48, 0x60, 0x44,
   0x60, 0x20, 0x40, 0x20, 0x00, 0x10, 0x00, 0x00 };
"""

arrow_left_mask = """
#define arrow_left_mask_width 16
#define arrow_left_mask_height 16
static unsigned short arrow_left_mask_bits[] = {
   0x0000, 0x0000, 0x0100, 0x0180, 0x01c0, 0x01e0, 0x01f0, 0x01f8, 0x01f8,
   0x01f0, 0x01e0, 0x01c0, 0x0180, 0x0100, 0x0000, 0x0000 };
"""

arrow_left = """
#define arrow_left_width 16
#define arrow_left_height 16
static unsigned short arrow_left_bits[] = {
   0x0000, 0x0000, 0x0100, 0x0180, 0x01c0, 0x01e0, 0x01f0, 0x01f8, 0x01f8,
   0x01f0, 0x01e0, 0x01c0, 0x0180, 0x0100, 0x0000, 0x0000 };
"""

arrow_right_mask = """
#define arrow_right_mask_width 16
#define arrow_right_mask_height 16
static unsigned short arrow_right_mask_bits[] = {
   0x0000, 0x0000, 0x0080, 0x0180, 0x0380, 0x0780, 0x0f80, 0x1f80, 0x1f80,
   0x0f80, 0x0780, 0x0380, 0x0180, 0x0080, 0x0000, 0x0000 };
"""

arrow_right = """
#define arrow_right_width 16
#define arrow_right_height 16
static unsigned short arrow_right_bits[] = {
   0x0000, 0x0000, 0x0080, 0x0180, 0x0380, 0x0780, 0x0f80, 0x1f80, 0x1f80,
   0x0f80, 0x0780, 0x0380, 0x0180, 0x0080, 0x0000, 0x0000 };
"""
