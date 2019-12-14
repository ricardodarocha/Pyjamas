program projPy;

uses
  Vcl.Forms,
  uRunPython in 'uRunPython.pas' {frmRunPython};

{$R *.res}

begin
  Application.Initialize;
  Application.MainFormOnTaskbar := True;
  Application.CreateForm(TfrmRunPython, frmRunPython);
  Application.Run;
end.
