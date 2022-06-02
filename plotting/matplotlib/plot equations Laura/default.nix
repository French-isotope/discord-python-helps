let pkgs = import ./nixpkgs.nix {};
  pythonEnv = pkgs.python310.withPackages(p : [p.matplotlib p.numpy p.math p.copy]);
in pkgs.mkShell {
  buildInputs = [ pythonEnv ];
}
