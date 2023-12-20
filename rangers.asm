// ; Definitions
arch    md.cpu
endian  msb

// ; Patched Output
output  "bin/Mighty Morphin Power-BR.bin",create

    table "tbl/geral.tbl"
// ; Configuration
    insert "tbl/geral.tbl"
constant CONFIG_LANGUAGE(PORTUGUESE)

define   CONFIG_ROM_NAME("POWER RANGERS 2             ")
define   CONFIG_ROM_REGION("U")
define   CONFIG_ROM_SIZE(eof)


origin ROM_START
    // ; Original File
    insert "bin/Mighty Morphin Power Rangers - The Movie (U) [!].bin"
    
    // ; Includes
    include "asm/macros.asm"
    include "asm/constants.asm"

if (CONFIG_LANGUAGE == ENGLISH) {

   // include "text/en/intro.asm"
    
}
    table "tbl/geral.tbl"

if (CONFIG_LANGUAGE == PORTUGUESE) {

    

    define   CONFIG_ROM_NAME("POWER RANGERS 2")
    define   CONFIG_ROM_REGION("U")

    
    include "text/br/intro.asm"
    include "text/br/script.asm"
    
   
}

include "asm/pointers.asm"

origin $00000150
    db {CONFIG_ROM_NAME}

origin $000001A4
    dl {CONFIG_ROM_SIZE}

origin $000001F0
    db {CONFIG_ROM_REGION}

    define CONFIG_ROM_SIZE(pc())
origin $026AE8
    jmp     font_16x16_hack

origin $026186
    jmp     revert_font16x16_hack

origin $1FF000
font_16x16_hack:
    save_registers_to_sp()
    move.l  #$6D600002,(VDP_CTRL).l
    lea     (font_16x16).l,a0
    jsr     (NEMESIS_DECOMPRESSOR).l
    load_registers_from_sp()

_load_chars_to_tilemap:
    move.l  d4,(VDP_CTRL).l
    move.w  (a0)+,d6
    cmp     #$E56B,d6
    beq     ++
    cmp     #$E5A0,d6
    bge     +
    cmp     #$E586,d6
    bge     ++
+
    cmp     #$E5B0,d6
    bge     +
    move.w  d6,(VDP_DATA).l
    cmp     #$E5A0,d6
    bge     ++
    add.w   #$1A,d6
+
    swap    d4
    add.w   #$80,d4
    swap    d4
    move.l  d4,(VDP_CTRL).l
    move.w  d6,(VDP_DATA).l
    swap    d4
    sub.w   #$80,d4
    swap    d4
+
    swap    d4
    add.w   #$02,d4
    swap    d4
    dbf     d7,_load_chars_to_tilemap
    clr.l   d6
    jmp     ($026AF2).l

revert_font16x16_hack:
    save_registers_to_sp()
    move.l  #$6D600002,(VDP_CTRL).l
    lea     (ORIGINAL_FONT).l,a0
    jsr     (NEMESIS_DECOMPRESSOR).l
    load_registers_from_sp()
    lea     (PRESS_START_TEXT).l,a6
    jmp     ($02618C).l

origin $1F6840
insert font_16x16,"gfx/fonte_16x16.nemesis.smd"
eof: