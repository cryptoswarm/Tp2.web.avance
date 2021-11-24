import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditAquaComponent } from './edit-aqua.component';

describe('EditAquaComponent', () => {
  let component: EditAquaComponent;
  let fixture: ComponentFixture<EditAquaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EditAquaComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(EditAquaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
