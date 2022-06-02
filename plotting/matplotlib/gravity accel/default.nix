let pkgs = import ./nixpkgs.nix {};
  pythonEnv = pkgs.python310.withPackages(p : [p.matplotlib]);
in pkgs.mkShell {
  buildInputs = [ pythonEnv ];
}
