let pkgs = import ./nixpkgs.nix {};
  pythonEnv = pkgs.python310.withPackages(p : [p.matplotlib p.dateutils p.psutil p.pyttsx3]);
in pkgs.mkShell {
  buildInputs = [ pythonEnv ];
}
