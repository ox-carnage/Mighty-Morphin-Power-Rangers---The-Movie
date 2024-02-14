// Control Macros

macro text(TEXT) {
    table "tbl/intro.tbl"
    dw {TEXT}
}

macro script_scene(TEXT) {
    table "tbl/intro.tbl"
    dw {TEXT}
}

macro script_historia(TEXT) {
    table "tbl/historia.tbl"
    dw {TEXT}
}

macro script_text(TEXT) {
    table "tbl/geral.tbl"
    db {TEXT}
}

macro script_menu(TEXT) {
    table "tbl/menu.tbl"
    dw {TEXT}
}

macro endstring() {
    dw ENDSTRING
}

macro delay() {
    dw DELAY
}

macro save_registers_to_sp() {
    movem.l #$FFFF,-(a7)
}

macro load_registers_from_sp() {
    movem.l (a7)+,#$FFFF
}