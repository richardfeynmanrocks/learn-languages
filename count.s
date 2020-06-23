; ============================================================
; count.s
;
; Counts to 5 in the R1 register. My first ARM UAL program.
; ============================================================

START
		ADD		R1, R1, #1
MAIN
		CMP		R1, #5
		BLT		START
